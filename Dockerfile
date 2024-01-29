FROM python:3.8-slim

WORKDIR /app

COPY pi.py .

CMD ["python", "pi.py"]
