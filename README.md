# txt2pdf
The project convert txt file to pdf.
The structure of the project is as foolows:
  A txt file gets uploaded to a source bucket in s3.
  A lambda function gets triggered and sends a "mission" to SQS.
  The code pulls missions from SQS, converts txt to pdf, uploads the pdf to a destenation bucket and send a email using SNS with a presigned url to the object in the       destenation bucket.
Folder cloudFormation templates contains all of theprojects templates.
Folder s3LambdaZip contains the code of the lambda that's used in the project.
