# Dockerfile

# pull the official docker image
FROM python:3.9.6-alpine

# set work directory
RUN mkdir /app
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app

# run entrypoint.sh
CMD [ "python", "main.py" ]