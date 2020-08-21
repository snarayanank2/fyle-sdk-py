"""
Reimbursements API
"""
from typing import Dict

from ..api_base import ApiBase


class Reimbursements(ApiBase):
    """Class for Reimbursements APIs."""

    GET_REIMBURSEMENTS = '/v3/reimbursements'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get Reimbursements
        :param limit: No. of reimbursements to be fetched
        :param offset: Pagination offset
        :return: List of Reimbursement Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_REIMBURSEMENTS)
