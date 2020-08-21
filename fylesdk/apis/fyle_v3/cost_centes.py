"""
CostCenters v3
"""
from typing import List, Dict

from ..api_base import ApiBase


class CostCenters(ApiBase):
    """Class for CostCenters APIs."""

    POST_COST_CENTERS = '/v3/cost_centers'
    GET_COST_CENTERS = '/v3/cost_centers'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get CostCenters
        :param limit: No of cost_centers to be fetched
        :param offset: Pagination offset
        :return: List of CostCenter Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_COST_CENTERS)

    def post(self, data: List[Dict], test: bool = False) -> Dict:
        """
        Post CostCenters
        :param data: List of CostCenter Objects to be Created
        :param test: Test Post of CostCenters
        :return: List of CostCenter Objects Created
        """
        return self._post_request(data={
            'data': data,
            'test': test
        }, api_url=self.POST_COST_CENTERS)
