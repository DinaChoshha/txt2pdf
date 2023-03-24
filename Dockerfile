From python:3

WORKDIR /txt2pdf

Run pip install boto3
Run pip install fpdf

COPY txt2pdf.py .

CMD "python3"

# this image has been built and push to docker hub.
# here is the link: https://hub.docker.com/r/dinachoshha/txt2pdf/tags
