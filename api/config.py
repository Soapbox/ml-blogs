"""The configuration file to use for the project."""

import os

if os.environ.get("USE_PRODUCTION_ENV"):
    # Database Credentials (Prod)
    db_private_ip = "<replace_me>"
    db_username = "<replace_me>"
    db_password = "<replace_me>"
    db_database_name = "<replace_me>"

    # AWS Credentials (Prod)
    aws_public_key = "<replace_me>"
    aws_secret_key = "<replace_me>"
    aws_region = "<replace_me>"
    aws_bucket_name = "<replace_me>"

    # API Keys (Prod)
    yelp_api_key = "rVQRrwc46ifXIGVrHwnk-wQRNvJCtgM_AdGAIUliu0fgEFIRP99Nybz2S01moBqYBxI4E9YH1maWlEA0itZf41Zb8vxioLzRRSyKOtTn00B_SmyNkUx-Nw6ft6NVXXYx" #pylint: disable=line-too-long
else:
    # Database Credentials (Dev)
    db_private_ip = "db"
    db_username = "ml"
    db_password = "secret"
    db_database_name = "machine_learning"

    # AWS Credentials (Dev)
    aws_public_key = "AKIAT7WYARTB3WGQ3YAV"
    aws_secret_key = "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"
    aws_region = "us-west-2"
    aws_bucket_name = "ml-staging-local"

    # API Keys (Dev)
    yelp_api_key = "rVQRrwc46ifXIGVrHwnk-wQRNvJCtgM_AdGAIUliu0fgEFIRP99Nybz2S01moBqYBxI4E9YH1maWlEA0itZf41Zb8vxioLzRRSyKOtTn00B_SmyNkUx-Nw6ft6NVXXYx" #pylint: disable=line-too-long
