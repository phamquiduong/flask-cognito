FROM public.ecr.aws/lambda/python:3.11

LABEL maintainer="CDK Lambda Flask"

RUN pip3 install --no-cache-dir --upgrade pip

# Install python dependencies
COPY ../requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /src

# Copy function code
COPY ../src /src
WORKDIR /src

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.handler" ]
