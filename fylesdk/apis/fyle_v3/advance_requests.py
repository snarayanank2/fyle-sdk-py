"""
AdvanceRequests API
"""
from typing import Dict

from ..api_base import ApiBase


class AdvanceRequests(ApiBase):
    """Class for AdvanceRequests APIs."""

    GET_ADVANCE_REQUESTS = '/v3/advance_requests'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get AdvanceRequests
        :param limit: No. of advance_requests to be fetched
        :param offset: Pagination offset
        :return: List of AdvanceRequest Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_ADVANCE_REQUESTS)
