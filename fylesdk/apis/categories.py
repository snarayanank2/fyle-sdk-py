from .api_base import ApiBase
from ..utils import get_request

class Categories(ApiBase):
    """Class for Categories APIs."""

    GET_CATEGORIES = '/api/tpa/v1/categories'
  
    def get(self, active_only=None):
        """Get a list of the existing Categories in the Organization.

        Parameters:
            active_only (bool): When set as false, the result will include all the Categories for the organization. (optional)

        Returns:
            List with dicts in Categories schema.
        """
        return get_request({
            'active_only': active_only
        }, Categories.GET_CATEGORIES, self._access_token)