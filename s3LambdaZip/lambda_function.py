import json
import boto3

def lambda_handler(event, context):  #required
   
    sqs = boto3.client('sqs')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/166145399123/fileConvertMessagesSqs",
        MessageBody='{0} {1}'.format(bucket, key)
    )
   
    return {
        'statusCode': 200,
        'body': 'success'
    }