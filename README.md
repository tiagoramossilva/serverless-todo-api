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

## 🧱 Architecture Diagram
<img width="642" height="72" alt="architecture drawio" src="https://github.com/user-attachments/assets/6a159803-97ac-4767-b20b-3cb186a25f96" />
