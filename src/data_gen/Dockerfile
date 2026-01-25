FROM python:3.13-slim

WORKDIR /app

COPY src/data_gen/generator.py .
COPY config/config.py .

RUN pip install psycopg2-binary

CMD ["python", "generator.py"]
