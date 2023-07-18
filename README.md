# Emailing Service using AWS
## About:

This project utilizes AWS services such as API Gateway, SQS, Lambda and SES in an Event driven fashion to send emails to a recipient from an S3 static website(consists of a form). The architecture follows AWS practices for Asynchoronous invocations of Lambda functions by using SQS Queues, hence decoupling the Lambda function and the API Gateway.

Architecture:
![Alt text](APIGateway_Arch.jpg)