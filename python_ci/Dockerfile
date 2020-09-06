FROM python:3.8-slim

COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
  && pip install --no-cache-dir -r requirements.txt \
  && pip install --no-cache-dir -r requirements-dev.txt
