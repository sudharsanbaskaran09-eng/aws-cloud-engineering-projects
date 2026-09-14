import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("aws-serverless-tasks")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    http_method = event.get("httpMethod", "")

    # CREATE TASK
    if http_method == "POST":
        body = json.loads(event.get("body", "{}"))

        task_id = str(uuid.uuid4())

        item = {
            "taskId": task_id,
            "title": body.get("title", ""),
            "description": body.get("description", ""),
            "status": body.get("status", "pending")
        }

        table.put_item(Item=item)

        return response(201, item)

    # GET ALL TASKS
    elif http_method == "GET":
        result = table.scan()

        return response(200, result.get("Items", []))

    # UPDATE TASK
    elif http_method == "PUT":
        body = json.loads(event.get("body", "{}"))
        task_id = body.get("taskId")

        if not task_id:
            return response(400, {
                "message": "taskId is required"
            })

        update_result = table.update_item(
            Key={
                "taskId": task_id
            },
            UpdateExpression="""
                SET #title = :title,
                    #description = :description,
                    #status = :status
            """,
            ExpressionAttributeNames={
                "#title": "title",
                "#description": "description",
                "#status": "status"
            },
            ExpressionAttributeValues={
                ":title": body.get("title", ""),
                ":description": body.get("description", ""),
                ":status": body.get("status", "pending")
            },
            ReturnValues="ALL_NEW"
        )

        return response(
            200,
            update_result["Attributes"]
        )

    # DELETE TASK
    elif http_method == "DELETE":
        body = json.loads(event.get("body", "{}"))
        task_id = body.get("taskId")

        if not task_id:
            return response(400, {
                "message": "taskId is required"
            })

        table.delete_item(
            Key={
                "taskId": task_id
            }
        )

        return response(200, {
            "message": "Task deleted successfully",
            "taskId": task_id
        })

    # INVALID METHOD
    else:
        return response(405, {
            "message": "Method not allowed"
        })


