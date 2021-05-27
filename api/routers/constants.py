"""Common constants used throughout the routers module."""

from .blogs import router as blogs_router

# router configuration
ROUTERS = [blogs_router]
PREFIXES = ["/blogs"]
TAGS = [["blogs"]]
