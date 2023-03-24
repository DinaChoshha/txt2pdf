# txt2pdf
The project converts txt file to pdf.  
The structure of the project is as follows:  
    A txt file gets uploaded to a source bucket in s3.  
    A lambda function gets triggered and sends a "mission" to SQS.  
    The code pulls missions from SQS, converts txt to pdf, uploads the pdf to a destenation bucket and send a email using SNS with a presigned url to the object in the       destenation bucket.  
Folder cloudFormation templates contains all of theprojects templates.  
Folder s3LambdaZip contains the code of the lambda that's used in the project.  
txt2pdf.py is the python code using boto3 that is in charge of convertin files.  
