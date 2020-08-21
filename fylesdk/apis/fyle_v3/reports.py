"""
Reports API
"""
from typing import Dict

from ..api_base import ApiBase


class Reports(ApiBase):
    """Class for Reports APIs."""

    GET_REPORTS = '/v3/reports'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Reports
        :param limit: No. of reports to be fetched
        :param offset: Pagination offset
        :return: List of Report Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_REPORTS)
