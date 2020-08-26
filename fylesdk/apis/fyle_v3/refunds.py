"""
Refunds API
"""
from typing import Dict

from ..api_base import ApiBase


class Refunds(ApiBase):
    """Class for Refunds APIs."""

    GET_REFUNDS = '/v3/refunds'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Refunds
        :param limit: No. of refunds to be fetched
        :param offset: Pagination offset
        :return: List of Refund Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_REFUNDS)
