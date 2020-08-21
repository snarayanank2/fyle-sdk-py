"""
TripRequests API
"""
from typing import Dict

from ..api_base import ApiBase


class TripRequests(ApiBase):
    """Class for TripRequests APIs."""

    GET_TRIP_REQUESTS = '/v3/trip_requests'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get TripRequests
        :param limit: No. of trip_requests to be fetched
        :param offset: Pagination offset
        :return: List of TripRequest Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_TRIP_REQUESTS)
