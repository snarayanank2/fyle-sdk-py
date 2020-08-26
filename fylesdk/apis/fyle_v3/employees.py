"""
Employees v3
"""
from typing import List, Dict

from ..api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    POST_EMPLOYEES = '/v3/employees'
    GET_EMPLOYEES = '/v3/employees'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Employees
        :param limit: No. of employees to be fetched
        :param offset: Pagination offset
        :return: List of Employee Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_EMPLOYEES)

    def post(self, data: List[Dict], test: bool = False) -> Dict:
        """
        Post Employees
        :param data: List of Employee Objects to be Created
        :param test: Test Post of Employees
        :return: List of Employee Objects Created
        """
        return self._post_request(data={
            'data': data,
            'test': test
        }, api_url=self.POST_EMPLOYEES)
