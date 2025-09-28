FROM python:3.10-slim

WORKDIR /app

COPY calculator.py .
COPY test.py .

RUN python test.py

CMD ["python", "calculator."]