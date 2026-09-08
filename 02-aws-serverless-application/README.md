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
