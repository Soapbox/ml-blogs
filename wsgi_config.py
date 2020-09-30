"""This file contains the configuration file for the WSGI."""

import os
from multiprocessing import cpu_count

# Standard configurations
bind = ":8500"
reload = not os.environ.get("USE_PRODUCTION_ENV")
print_config = not os.environ.get("USE_PRODUCTION_ENV")

# Worker and thread configurations
worker_class = "gthread"
workers = 1 * cpu_count()
thread = 1 * cpu_count()
timeout = 360
preload = True
