FROM python:3.8.12-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /api

COPY requirements.txt /api/
RUN apt update && pip install -r requirements.txt
COPY . /api/