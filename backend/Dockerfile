FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code


RUN pip install --upgrade pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2


COPY requirements.txt /code/
RUN pip install -r requirements.txt


COPY . /code/
