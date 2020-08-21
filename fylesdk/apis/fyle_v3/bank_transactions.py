"""
BankTransactions API
"""
from typing import Dict

from ..api_base import ApiBase


class BankTransactions(ApiBase):
    """Class for BankTransactions APIs."""

    GET_BANK_TRANSACTIONS = '/v3/bank_transactions'

    def get(self, limit: int = None, offset: int = None, **kwargs) -> Dict:
        """
        Get BankTransactions
        :param limit: No. of bank_transactions to be fetched
        :param offset: Pagination offset
        :return: List of BankTransaction Objects
        """
        return self._get_request(params={
            'limit': limit,
            'offset': offset,
            **kwargs
        }, api_url=self.GET_BANK_TRANSACTIONS)
