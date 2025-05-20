# Chapter 10 - Orchestrating the Data Pipeline

In this chapter, we looked at a critical part of a data engineers job: designing and
orchestrating data pipelines. First, we examined some of the core concepts around data
pipelines, such as the definition of a DAG (directed acyclic graph), 
and common pipeline triggers (scheduled and event-based pipelines). We also 
looked at how to handle failures and retries.

We then looked at four different AWS services that can be used for creating and
orchestrating data pipelines. This included Amazon Data Pipeline (now in maintenance mode), 
AWS Glue Workflows, Amazon Managed Workflows for Apache Airflow (MWAA), and AWS Step Functions.
We discussed some of the use cases for each of these services, as well as the pros and cons
of them.

## Hands-on Activity
In the hands-on section of this chapter, we built an event-driven pipeline. We used
two AWS Lambda functions for processing files, and an Amazon SNS topic for sending out
notifications about failure. Then, we put these pieces of our data pipeline together into
a state machine orchestrated by AWS Step Functions.

#### Lambda function to determine the file extension

- AWS Management Console - Lambda Functions: https://console.aws.amazon.com/lambda/home

- Code for Lambda function to check file extension: [dataeng-check-file-ext.py](dataeng-check-file-ext.py)

#### Lambda function to randomly generate failures

- Code for Lambda function to generate random failures: [dataeng-random-failure-generator.py](dataeng-random-failure-generator.py)

#### Creating an SNS topic and subscribing to an email address

- AWS Management Console - SNS: https://us-east-2.console.aws.amazon.com/sns/v3/home

#### Creating a new Step Functions state machine

- AWS Management Console - Step Functions: https://console.aws.amazon.com/states/home

- Example of Step Functions JSON for completed state machine: [ProcessFileStateMachine.json](ProcessFileStateMachine.json)  
  [Note that the ARN references in this state machine are not valid, and would need to be updated to reflect your AWS account number]

#### Configuring our S3 bucket to send events to EventBridge

- AWS Management Console - Amazon S3: https://s3.console.aws.amazon.com/s3

#### Create an EventBridge rule for triggering our Step Functions state machine

- AWS Management Console - EventBridge: https://console.aws.amazon.com/events/home

#### Testing out event-driven data orchestration pipeline

- AWS Management Console - Amazon S3: https://s3.console.aws.amazon.com/s3

