FROM python:3.9-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create static folder if it doesn't exist
RUN mkdir -p static/gen

# Set environment variables
ENV PORT=8000
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV SEND_FILE_MAX_AGE_DEFAULT=0

# Start the application
CMD gunicorn test:app \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --threads 2 \
    --timeout 30 \
    --reload \
    --access-logfile - \
    --error-logfile -
