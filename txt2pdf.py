import boto3
import os
from fpdf import FPDF


sqsClient = boto3.client('sqs')
s3Client = boto3.client('s3')
snsClient = boto3.client('sns')

queueUrl = sqsClient.get_queue_url(QueueName='fileConvertMessagesSqs')['QueueUrl']

while (True):
    response = sqsClient.receive_message(
        QueueUrl=queueUrl,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )

    messages = response.get('Messages', [])
    for message in messages:
        messageBody = message['Body']
        messageArr = messageBody.split()

        sourceBucket = messageArr[0]
        objectName = messageArr[1]

        fileName = objectName.split('.')[0]

        s3Client.download_file(sourceBucket, objectName, fileName+'.txt')
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(fileName+'.txt', "r") as f:
            pdf_content = f.read()

        pdf.write(5, pdf_content)
        pdf.output(fileName+'.pdf')

        destinationBucket = 'destination-pdf-bucket-dina-choshha'
        response = s3Client.upload_file(fileName+'.pdf', destinationBucket, fileName+'.pdf')

        os.remove(fileName+'.pdf')
        os.remove(fileName+'.txt')

        s3Client.delete_object(Bucket=sourceBucket, Key=fileName+'.txt')

        receiptHandle = message['ReceiptHandle']
        sqsClient.delete_message(QueueUrl=queueUrl, ReceiptHandle=receiptHandle)

        topicName = "ConvertedPdfsTopic"

        url = s3Client.generate_presigned_url(
            'get_object',
            Params={'Bucket': destinationBucket, 'Key': fileName+'.pdf'},
            ExpiresIn=86400)

        response = snsClient.publish(
            TopicArn='arn:aws:sns:us-east-1:166145399123:' + topicName,
            Message='You have a new converted pdf in the following link, the link will expire in a day. {0}'.format(url),
            Subject='New converted pdf'
        )

