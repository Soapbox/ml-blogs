# Base image
FROM python:3.6

ENV PYTHONFAULTHANDLER=1 \
PYTHONUNBUFFERED=1 \
PYTHONHASHSEED=random \
PIP_NO_CACHE_DIR=off \
PIP_DISABLE_PIP_VERSION_CHECK=on \
PIP_DEFAULT_TIMEOUT=100

# Install project dependencies
WORKDIR /app/ml-blogs
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy rest of API files into container
COPY . /app/ml-blogs

CMD [ "/bin/sh", "-c", "gunicorn --config wsgi_config.py wsgi:app" ]
