FROM python:3.9

ENV PYTHONDONTWRITEYBTECODE=1
ENV PYTHONUNBBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt



# Bibliotecas de Sistema
RUN apt-get update