"""
Advances API
"""
from typing import Dict

from ..api_base import ApiBase


class Advances(ApiBase):
    """Class for Advances APIs."""

    GET_ADVANCES = '/v3/advances'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Advances
        :param limit: No. of advances to be fetched
        :param offset: Pagination offset
        :return: List of Advance Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_ADVANCES)
