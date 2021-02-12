"""Common constants used inside the database module."""

import os
from api.config import db_username, db_password, db_private_ip, db_database_name

# database configuration
DATABASE_CREDENTIALS = (
    f"{db_username}:{db_password}@{db_private_ip}:3306/{db_database_name}"
)
DATABASE_URL = f"mysql+pymysql://{DATABASE_CREDENTIALS}"
if os.environ.get("IS_UNIT_TEST"):
    DATABASE_URL = "sqlite:///:unit_test:"
