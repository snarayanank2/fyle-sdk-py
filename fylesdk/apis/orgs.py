from .api_base import ApiBase

class Orgs(ApiBase):
    """Class for Orgs APIs."""

    GET_ORGS = '/api/tpa/v1/orgs'

    def get(self):
        """Get the details of the current authorized Org.

        Parameters:
            None

        Returns:
            List with dicts in Orgs schema.
        """
        return self._get_request({}, Orgs.GET_ORGS)