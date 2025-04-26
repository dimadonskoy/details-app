# Base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/sites-enabled/default
COPY details_nginx.conf /etc/nginx/sites-enabled/default

RUN chmod +x start_gunicorn.sh

EXPOSE 80

CMD ["bash", "-c", "service nginx start && ./start_gunicorn.sh && tail -f /dev/null"]

