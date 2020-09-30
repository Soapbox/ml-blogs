"""The main WSGI codebase for connecting with the Flask application."""

from api.app import app


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
