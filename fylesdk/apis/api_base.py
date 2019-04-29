
class ApiBase:
    """The base class for all API classes."""

    def __init__(self):
        self._access_token = None

    def change_access_token(self, access_token):
        """Change the old access token with the new one.
        
        Parameters:
            access_token (str): The new access token.
        """
        self._access_token = access_token
