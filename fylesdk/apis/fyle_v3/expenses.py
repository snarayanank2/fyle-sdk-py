"""
Expenses API
"""
from typing import Dict

from ..api_base import ApiBase


class Expenses(ApiBase):
    """Class for Expenses APIs."""

    GET_EXPENSES = '/v3/expenses'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Expenses
        :param limit: No. of expenses to be fetched
        :param offset: Pagination offset
        :return: List of Expense Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_EXPENSES)
