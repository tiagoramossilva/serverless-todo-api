# Serverless To-Do API

## Architecture
API Gateway -> Lambda -> DynamoDB

## Tech Stack
- AWS Lambda
- API Gateway
- DynamoDB
- IAM

## Endpoints

POST /tasks
GET /tasks
DELETE /tasks?id={id}

## Features
- Create tasks
- List tasks
- Delete tasks

## Decisions
- Serverless architecture for scalability
- DynamoDB for low-latency NoSQL storage
- IAM with least privilege
