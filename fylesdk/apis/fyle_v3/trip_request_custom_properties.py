"""
TripRequestCustomProperties API
"""
from typing import Dict

from ..api_base import ApiBase


class TripRequestCustomProperties(ApiBase):
    """Class for TripRequestCustomProperties APIs."""

    GET_TRIP_REQUEST_CUSTOM_PROPERTIES = '/v3/trip_request_custom_properties'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get TripRequestCustomProperties
        :param limit: No. of trip_request_custom_properties to be fetched
        :param offset: Pagination offset
        :return: List of TripRequestCustomProperty Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_TRIP_REQUEST_CUSTOM_PROPERTIES)
