"""
Categories API
"""
from typing import Dict

from ..api_base import ApiBase


class Categories(ApiBase):
    """Class for Categories APIs."""

    GET_CATEGORIES = '/v3/categories'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Categories
        :param limit: No. of categories to be fetched
        :param offset: Pagination offset
        :return: List of Category Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_CATEGORIES)
