# AWS Serverless Task Management API

A serverless REST API for creating, retrieving, updating, and deleting tasks using **Amazon API Gateway, AWS Lambda, and Amazon DynamoDB**.

This project demonstrates how to build and deploy a fully serverless backend without managing traditional servers.

---

## Architecture

```text
                    ┌──────────────────────┐
                    │       Client         │
                    │   Postman / Browser  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Amazon API        │
                    │       Gateway        │
                    │                      │
                    │  POST /tasks         │
                    │  GET    /tasks       │
                    │  PUT    /tasks       │
                    │  DELETE /tasks       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      AWS Lambda      │
                    │ aws-serverless-      │
                    │     task-api         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Amazon           │
                    │     DynamoDB         │
                    │ aws-serverless-tasks │
                    └──────────────────────┘
```

---

## AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon API Gateway | Exposes REST API endpoints |
| AWS Lambda | Executes serverless application logic |
| Amazon DynamoDB | Stores task data |
| AWS IAM | Provides permissions to Lambda |
| Amazon CloudWatch | Monitors Lambda execution logs |

---

## Project Structure

```text
02-aws-serverless-application/
│
├── lambda/
│   └── handler.py
│
└── README.md
```

---

## AWS Resources

### DynamoDB

**Table Name:**

```text
aws-serverless-tasks
```

**Partition Key:**

```text
taskId
```

**Key Type:**

```text
String
```

**Capacity Mode:**

```text
On-Demand
```

---

### AWS Lambda

**Function Name:**

```text
aws-serverless-task-api
```

**Runtime:**

```text
Python 3.12
```

**Architecture:**

```text
x86_64
```

**IAM Role:**

```text
aws-serverless-lambda-role
```

---

### API Gateway

**API Name:**

```text
aws-serverless-task-api
```

**API Type:**

```text
REST API
```

**Resource:**

```text
/tasks
```

**Stage:**

```text
dev
```

**Invoke URL:**

```text
https://hmf8166154.execute-api.us-east-1.amazonaws.com/dev
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| PUT | `/tasks` | Update an existing task |
| DELETE | `/tasks` | Delete a task |

---

# API Operations

## 1. Create a Task

### Request

```http
POST /tasks
```

### Request Body

```json
{
  "title": "Build AWS Serverless API",
  "description": "Create a task management API using Lambda, API Gateway and DynamoDB",
  "status": "pending"
}
```

### Response

```json
{
  "taskId": "generated-uuid",
  "title": "Build AWS Serverless API",
  "description": "Create a task management API using Lambda, API Gateway and DynamoDB",
  "status": "pending"
}
```

**HTTP Status:**

```text
201 Created
```

---

## 2. Get All Tasks

### Request

```http
GET /tasks
```

### Response

```json
[
  {
    "taskId": "generated-uuid",
    "title": "Build AWS Serverless API",
    "description": "Create a task management API using Lambda, API Gateway and DynamoDB",
    "status": "pending"
  }
]
```

**HTTP Status:**

```text
200 OK
```

---

## 3. Update a Task

### Request

```http
PUT /tasks
```

### Request Body

```json
{
  "taskId": "generated-uuid",
  "title": "Build AWS Serverless API - Updated",
  "description": "Build and test a serverless task management API",
  "status": "completed"
}
```

### Response

```json
{
  "taskId": "generated-uuid",
  "title": "Build AWS Serverless API - Updated",
  "description": "Build and test a serverless task management API",
  "status": "completed"
}
```

**HTTP Status:**

```text
200 OK
```

---

## 4. Delete a Task

### Request

```http
DELETE /tasks
```

### Request Body

```json
{
  "taskId": "generated-uuid"
}
```

### Response

```json
{
  "message": "Task deleted successfully",
  "taskId": "generated-uuid"
}
```

**HTTP Status:**

```text
200 OK
```

---

# Lambda Function

The Lambda function implements the complete CRUD workflow.

```text
POST    → Create Task
GET     → Retrieve Tasks
PUT     → Update Task
DELETE  → Delete Task
```

The application automatically generates a unique UUID for every newly created task.

---

# IAM Configuration

The Lambda execution role is:

```text
aws-serverless-lambda-role
```

The role contains the following policies:

```text
AWSLambdaBasicExecutionRole
AmazonDynamoDBFullAccess
```

### AWSLambdaBasicExecutionRole

Allows the Lambda function to write execution logs to Amazon CloudWatch.

### AmazonDynamoDBFullAccess

Allows the Lambda function to perform CRUD operations on the DynamoDB table.

> For production applications, permissions should be restricted to only the required DynamoDB actions and resources.

---

# Monitoring

Lambda execution logs are available in Amazon CloudWatch.

**Log Group:**

```text
/aws/lambda/aws-serverless-task-api
```

CloudWatch records Lambda execution information such as:

```text
START RequestId
END RequestId
REPORT RequestId
```

These logs provide visibility into Lambda execution and help with troubleshooting.

---

# Testing

The deployed API was tested using **Postman**.

### CRUD Testing

- POST request successfully created a task
- GET request successfully retrieved tasks
- PUT request successfully updated a task
- DELETE request successfully deleted a task
- DynamoDB verified the deletion
- Lambda execution logs verified in CloudWatch
- Public API Gateway endpoint tested successfully

---

# API Testing Flow

```text
POST /tasks
     │
     ▼
Create Task
     │
     ▼
DynamoDB
     │
     ▼
GET /tasks
     │
     ▼
Retrieve Task
     │
     ▼
PUT /tasks
     │
     ▼
Update Task
     │
     ▼
DELETE /tasks
     │
     ▼
DynamoDB
     │
     ▼
Task Removed
```

---

# Key Features

- Serverless REST API
- CRUD operations
- AWS Lambda backend
- API Gateway integration
- DynamoDB persistent storage
- Automatic UUID generation
- IAM-based access control
- CloudWatch monitoring
- API deployment using API Gateway stages
- On-demand DynamoDB capacity
- No traditional server management

---

# Learning Outcomes

This project provided practical experience with:

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch
- REST API development
- Serverless architecture
- CRUD application development
- API testing with Postman
- AWS resource configuration
- API deployment and monitoring

---

# Screenshots

The implementation screenshots for this project include:

| No. | Screenshot | Description |
|---|---|---|
| 01 | `01-dynamodb-table.png` | DynamoDB table configuration |
| 02 | `02-lambda-iam-role.png` | Lambda IAM role and permissions |
| 03 | `03-lambda-function.png` | Lambda function configuration |
| 04 | `04-api-gateway.png` | API Gateway configuration |
| 05 | `05-post-task-success.png` | POST task creation |
| 06 | `06-dynamodb-item-created.png` | DynamoDB item created |
| 07 | `07-get-tasks-success.png` | GET tasks response |
| 08 | `08-put-task-success.png` | PUT task update |
| 09 | `09-delete-task-success.png` | DELETE task response |
| 10 | `10-api-deployment.png` | API Gateway deployment |
| 11 | `11-public-post-success.png` | Public POST API test |
| 12 | `12-public-get-success.png` | Public GET API test |
| 13 | `13-public-put-success.png` | Public PUT API test |
| 14 | `14-public-delete-success.png` | Public DELETE API test |
| 15 | `15-dynamodb-delete-verification.png` | DynamoDB deletion verification |
| 16 | `16-cloudwatch-lambda-logs.png` | CloudWatch Lambda execution logs |

---

# Conclusion

The **AWS Serverless Task Management API** demonstrates how multiple AWS managed services can be combined to build a scalable serverless backend.

The application uses:

```text
Amazon API Gateway
        │
        ▼
AWS Lambda
        │
        ▼
Amazon DynamoDB
```

with **AWS IAM** for permissions and **Amazon CloudWatch** for monitoring.

This project demonstrates practical implementation of a serverless CRUD application on AWS and provides a foundation for building more advanced serverless applications.

---

## Author

**Sudharsan B**

Cloud | AWS | DevOps | Serverless

GitHub:

https://github.com/sudharsanbaskaran09-eng

