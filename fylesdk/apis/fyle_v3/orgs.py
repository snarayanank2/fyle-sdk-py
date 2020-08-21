"""
Orgs API
"""
from typing import Dict

from ..api_base import ApiBase


class Orgs(ApiBase):
    """Class for Orgs APIs."""

    GET_ORGS = '/v3/orgs'

    def get(self) -> Dict:
        """
        Get Orgs
        :return: List of Org Objects with Current org
        """
        return self._get_request(params={}, api_url=self.GET_ORGS)
