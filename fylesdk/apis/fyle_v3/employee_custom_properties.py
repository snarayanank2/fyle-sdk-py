"""
EmployeeCustomProperties API
"""
from typing import Dict

from ..api_base import ApiBase


class EmployeeCustomProperties(ApiBase):
    """Class for EmployeeCustomProperties APIs."""

    GET_EMPLOYEE_CUSTOM_PROPERTIES = '/v3/employee_custom_properties'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get EmployeeCustomProperties
        :param limit: No. of employee_custom_properties to be fetched
        :param offset: Pagination offset
        :return: List of EmployeeCustomProperty Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_EMPLOYEE_CUSTOM_PROPERTIES)
