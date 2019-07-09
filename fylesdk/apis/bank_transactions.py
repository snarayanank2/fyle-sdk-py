from .api_base import ApiBase

class BankTransactions(ApiBase):
    """Class for BankTransactions APIs."""

    POST_BankTransactions = '/api/tpa/v1/bank_transactions'
    GET_BankTransactions = '/api/tpa/v1/bank_transactions'

    def post(self, data):
        """Create or Update Bank Transactions in bulk.

        Parameters:
            data (list): List of dicts in BankTransactions schema.
        
        Returns:
            List with IDs from the new Bank Transactions.
        """
        return self._post_request(data, BankTransactions.POST_BankTransactions)

    def get(self):
        """Get a list of all Bank Transactions.

        Parameters:
            
        Returns:
            List with dicts in Bank Transactions schema.
        """
        return self._get_request({}, BankTransactions.GET_BankTransactions)
