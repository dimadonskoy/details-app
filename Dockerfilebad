FROM python:3.13-alpine AS base

# Copy app source code
COPY . /app

# Set working directory
WORKDIR /app

# Install build tools and pip dependencies
RUN apk add --no-cache build-base git python3-dev libffi-dev openssl-dev

# Create virtual environment
RUN python -m venv /app/venv

# Copy dependency file and install
RUN /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install -r requirements.txt

# Expose ports
EXPOSE 80

# Start services with virtualenv activated
CMD ["sh", "-c", ". /app/venv/bin/activate && nginx && ./start_gunicorn.sh && tail -f /dev/null"]
