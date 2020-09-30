"""Common utility functions used in the endpoints module."""

import json
from api.exceptions.error import raise_error

def validate_json_format(request_data):
    """
    Validates if the requested data follows the JSON format.

    Parameters:
        request_data: The data that was requested through the endpoint.

    Returns:
        The JSON that was requested through the endpoint as a dictionary.
    """
    try:
        return json.loads(request_data)
    except json.decoder.JSONDecodeError:
        raise_error(
            "UnprocessableEntity",
            "Unable to read JSON data. Please ensure that your data is correctly formatted.",
            status_code=422
        )

def validate_key_format(json_dict, key):
    """
    Validates if the requested data has the correct key.

    Parameters:
        json_dict: The JSON object that was requested through the endpoint as a dictionary.
        key: The key that is being validated in the JSON.

    Returns:
        The value that belongs to the key in the request.
    """

    try:
        return json_dict[key]
    except KeyError:
        raise_error(
            "UnprocessableEntity",
            "Unable to read JSON data. Please ensure that your data is correctly formatted.",
            status_code=422
        )

def validate_data_type(sample, key, data_type):
    """
    Validates if the key's value is the correct data type.

    Parameters:
        sample: The value of the given key that was requested through an endpoint.
        key: The key, as a string, that the value belongs to.
        data_type: The data type that the value should be.
    """
    if not isinstance(sample, data_type):
        raise_error(
            "UnprocessableDataType",
            f"Unable to process data type. Please ensure that the '{key}' value is a {data_type}.",
            status_code=422
        )
