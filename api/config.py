"""The configuration file to use for the project."""

import os

# Database Credentials (Prod)
db_private_ip = os.environ.get("DB_PRIVATE_IP")
db_username = os.environ.get("MYSQL_USER")
db_password = os.environ.get("MYSQL_PASSWORD")
db_database_name = os.environ.get("MYSQL_DATABASE")

# AWS Credentials (Prod)
aws_public_key = os.environ.get("AWS_PUBLIC_KEY")
aws_secret_key = os.environ.get("AWS_SECRET_KEY")
aws_region = os.environ.get("AWS_REGION")
aws_bucket_name = os.environ.get("AWS_BUCKET_NAME")
