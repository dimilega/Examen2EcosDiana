#!/bin/bash

FROM python:3.9.5-slim-buster   

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get -y install python3-pip python3-dev \    
    && apt-get -y install build-essential libssl-dev \ 
    && apt-get -y install libffi-dev python3-setuptools

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app

RUN ./gunicorn_starter.sh
