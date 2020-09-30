"""The error definition for general errors that can occur in API."""

class Error(Exception):
    """
    The Error class defines error messages and status codes that could occur.

    Parameters:
        error_type: The specific type of error that occurs.
        message: The error message that is output.
        status_code: The status code associated with the error.
        payload: The payload of the error.
    """

    def __init__(self, error_type, message, status_code=None, payload=None):
        super(Error, self).__init__()

        self.error_type = error_type
        self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        """
        Converts the payload with the message into a dictionary.
        Returns:
            The converted payload into a dictionary.
        """
        rv = dict(self.payload or ())
        rv["error_type"] = self.error_type
        rv["message"] = self.message

        return rv

def raise_error(error_type, error_message, status_code):
    """
    Raises error in API given the parameters in the Error object.

    Parameters:
        error_type: The specific type of error that occurs.
        message: The error message that is output.
        status_code: The status code associated with the error.
    """
    raise Error(error_type, error_message, status_code)
