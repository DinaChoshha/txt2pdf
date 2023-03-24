# txt2pdf
The project converts txt file to pdf.  
  
Folder cloudFormation templates contains all of theprojects templates.  
  
Folder s3LambdaZip contains the code of the lambda that's used in the project.  
  
txt2pdf.py is the python code using boto3 that is in charge of convertin files. 
  
Dockerfile is the file that's used to build the projects image. It was pushed to dockerhub (the link is in the file itself). the images contains all the necessaties for the txt2pdf.py to work (python3, boto3, fpdf).  
  
The structure of the project is as follows:  
    A txt file gets uploaded to a source bucket in s3.  
    A lambda function gets triggered and sends a "mission" to SQS.  
    The code pulls missions from SQS, converts txt to pdf, uploads the pdf to a destenation bucket and send a email using SNS with a presigned url to the object in the       destenation bucket.  
  
Commands to run the docker image in the ec2 instances:  
  docker pull dinachoshha/txt2pdf:1  
  docker run -it -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION  dinachoshha/txt2pdf:1 bash  
  python3 txt2pdf.py  
  
  
