from ..api_base import ApiBase


class Categories(ApiBase):
    """Class for Categories APIs."""

    GET_CATEGORIES = '/api/tpa/v1/categories'
    POST_CATEGORIES = '/api/tpa/v1/categories'

    def post(self, data):
        """Create or Update Categories in bulk.

        Parameters:
            data (list): List of dicts in Categories schema.

        Returns:
            List with IDs from the new and updated Categories.
        """
        return self._post_request(data, Categories.POST_CATEGORIES)
  
    def get(self, active_only=None, **kwargs):
        """Get a list of the existing Categories in the Organization.

        Parameters:
            active_only (bool): When set as false, the result will include all the Categories for the organization. (optional)

        Returns:
            List with dicts in Categories schema.
        """
        return self._get_request({
            'active_only': active_only,
            **kwargs
        }, Categories.GET_CATEGORIES)
