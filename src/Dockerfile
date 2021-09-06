FROM python:3.9.6-alpine3.14
LABEL maintainer="azat715"

RUN apk update 
RUN apk add --no-cache bash

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m pip install -r requirements.txt --no-cache-dir 
COPY . /code/