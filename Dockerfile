FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE 8000

CMD gunicorn test:app --bind 0.0.0.0:$PORT --workers 4 --threads 2 --timeout 60
