"""The super class and methods used in all endpoint unit test classes."""

import unittest
import json
from flask import Flask, jsonify
from api.exceptions.error import Error

class SuperTestCase(unittest.TestCase):
    """
    The parent class for all endpoint unit tests.

    Parameters:
        app: The Flask object that starts the Flask app.
        tester: The test client that enables Flask's testing client for app.
        http_method_get: The string that contains the HTTP method GET.
        http_method_post: The string that contains the HTTP method POST.
    """

    def __init__(self, *args, **kwargs):
        super(SuperTestCase, self).__init__(*args, **kwargs)

        self.app = Flask(__name__)
        self.tester = self.app.test_client()
        self.http_method_get = "GET"
        self.http_method_post = "POST"

        # Error handler
        @self.app.errorhandler(Error)
        def handle_invalid_usage(error):
            """
            An error handler for when there is an exception to be raised.

            Parameters:
                error: The error information to return back to the client.

            Returns:
                The wrapped response containing the error information.
            """
            response = jsonify(error.to_dict())
            response.status_code = error.status_code

            return response

    def generate_payload(self, request_data, endpoint, http_method):
        """
        Requests and dumps the payload as a JSON object.

        Parameters:
            request_data: The data that was requested through the endpoint.
            endpoint: The endpoint that is being requested.
            http_method: A string containing the HTTP method type.

        Returns:
            A tuple of the response's string output and status code.
        """
        if http_method == self.http_method_post:
            response = self.tester.post(
                endpoint,
                data=json.dumps(request_data),
                content_type="application/json"
            )
        elif http_method == self.http_method_get:
            response = self.tester.get(
                endpoint,
                data=json.dumps(request_data),
                content_type="application/json"
            )

        response_data = response.get_data(as_text=True)
        response_data = json.loads(response_data) if response_data else response_data

        return response_data, response.status_code

    def get_request_url(self, endpoint, url_parameters):
        """
        Produces a request URL given the URL parameters.

        Parameters:
            endpoint: The base endpoint that is being requested.
            url_parameters: The parameters that are being requested through the URL.

        Returns:
            The URL to request to the endpoint.
        """
        for parameter in url_parameters:
            endpoint += f"/{parameter}"

        return endpoint
