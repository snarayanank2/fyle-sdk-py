"""
ExpenseCustomProperties API
"""
from typing import Dict

from ..api_base import ApiBase


class ExpenseCustomProperties(ApiBase):
    """Class for ExpenseCustomProperties APIs."""

    GET_CATEGORIES = '/v3/expense_custom_properties'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get ExpenseCustomProperties
        :param limit: No. of expense_custom_properties to be fetched
        :param offset: Pagination offset
        :return: List of ExpenseCustomProperty Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_CATEGORIES)
