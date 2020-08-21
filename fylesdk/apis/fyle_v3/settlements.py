"""
Settlements API
"""
from typing import Dict

from ..api_base import ApiBase


class Settlements(ApiBase):
    """Class for Settlements APIs."""

    GET_SETTLEMENTS = '/v3/settlements'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Settlements
        :param limit: No. of settlements to be fetched
        :param offset: Pagination offset
        :return: List of Settlement Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_SETTLEMENTS)
