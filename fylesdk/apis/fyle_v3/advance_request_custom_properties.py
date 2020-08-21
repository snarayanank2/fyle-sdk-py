"""
AdvanceRequestCustomProperties API
"""
from typing import Dict

from ..api_base import ApiBase


class AdvanceRequestCustomProperties(ApiBase):
    """Class for AdvanceRequestCustomProperties APIs."""

    GET_ADVANCE_REQUEST_CUSTOM_PROPERTIES = '/v3/advance_request_custom_properties'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get AdvanceRequestCustomProperties
        :param limit: No. of advance_request_custom_properties to be fetched
        :param offset: Pagination offset
        :return: List of AdvanceRequestCustomProperty Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_ADVANCE_REQUEST_CUSTOM_PROPERTIES)
