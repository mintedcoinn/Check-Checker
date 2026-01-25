FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install psycopg2-binary

CMD ["python", "generator.py"]
