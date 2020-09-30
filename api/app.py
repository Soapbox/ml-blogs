"""The ML API's main application server codebase."""

import logging
from flask import Flask, jsonify
from .exceptions.error import Error
from .endpoints.blogs import blogs_api
from .endpoints.rescrape_blogs import rescrape_blogs_api

# Setup Flask main application server
app = Flask(__name__)

# Register blueprints
app.register_blueprint(blogs_api)
app.register_blueprint(rescrape_blogs_api)

# Main application routes
@app.route("/")
def hello():
    """The endpoint that is called when the base URL endpoint is called.

    Returns:
        A string to indicate that the application server works.
    """
    return "Welcome to Soapbox ML Next Steps API project!"

# Error handlers
@app.errorhandler(Error)
def handle_invalid_usage_error(error):
    """An general error handler for any error that could occur.

    Parameters:
        error: The error information to return back to the client.

    Returns:
        The wrapped response containing the error information.
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
