"""
Projects v3
"""
from typing import List, Dict

from ..api_base import ApiBase


class Projects(ApiBase):
    """Class for Projects APIs."""

    POST_PROJECTS = '/v3/projects'
    GET_PROJECTS = '/v3/projects'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Projects
        :param limit: No. of projects to be fetched
        :param offset: Pagination offset
        :return: List of Project Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_PROJECTS)

    def post(self, data: List[Dict], test: bool = False) -> Dict:
        """
        Post Projects
        :param data: List of Project Objects to be Created
        :param test: Test Post of Projects
        :return: List of Project Objects Created
        """
        return self._post_request(data={
            'data': data,
            'test': test
        }, api_url=self.POST_PROJECTS)
