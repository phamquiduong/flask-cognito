FROM python:3
ENV PYTHONUNBUFFERED 1


# Create code source code folder
RUN mkdir /src


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip


# Install python packet
COPY docker/flask/requirements-docker.txt /
RUN pip install -r requirements-docker.txt

COPY src/requirements.txt /
RUN pip install -r requirements.txt
