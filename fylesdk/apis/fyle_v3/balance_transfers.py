"""
BalanceTransfers API
"""
from typing import Dict

from ..api_base import ApiBase


class BalanceTransfers(ApiBase):
    """Class for BalanceTransfers APIs."""

    GET_BALANCE_TRANSFERS = '/v3/balance_transfers'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get BalanceTransfers
        :param limit: No. of balance_transfers to be fetched
        :param offset: Pagination offset
        :return: List of BalanceTransfer Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_BALANCE_TRANSFERS)
