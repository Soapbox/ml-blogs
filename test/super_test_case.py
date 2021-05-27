"""The super class and methods used in all endpoint unit test classes."""

from api.main import app
from api.db import LocalSession, engine
from fastapi.testclient import TestClient
import unittest
import json

class SuperTestCase(unittest.TestCase):
    """The parent class for all endpoint unit tests."""

    def __init__(self, *args, **kwargs):
        super(SuperTestCase, self).__init__(*args, **kwargs)

        self.engine = engine
        self.http_method_get = "GET"
        self.http_method_post = "POST"
        self.client = TestClient(app)
        self.session = LocalSession()

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
            response = self.client.post(
                endpoint,
                json=request_data
            )
        elif http_method == self.http_method_get:
            response = self.client.get(
                endpoint,
                json=request_data
            )

        return response.json(), response.status_code
