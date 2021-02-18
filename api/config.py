"""The configuration file to use for the project."""

import os

# Database Credentials (Prod)
db_private_ip = os.environ.get("DB_PRIVATE_IP")
db_username = os.environ.get("MYSQL_USER")
db_password = os.environ.get("MYSQL_PASSWORD")
db_database_name = os.environ.get("MYSQL_DATABASE")
