from .api_base import ApiBase


class CorporateCreditCardExpenses(ApiBase):
    """Class for BankTransactions APIs."""

    GET_CORPORATE_CREDIT_CARD_EXPENSES = '/api/tpa/v1/corporate_credit_card_expenses'
    GET_CORPORATE_CREDIT_CARD_EXPENSES_COUNT = '/api/tpa/v1/corporate_credit_card_expenses/count'

    def get(self, limit=None, offset=None, updated_at=None, spent_at=None, exported=None, personal=None, state=None,
            transaction_type=None, settlement_id=None, reimbursement_state=None):
        """Get a list of all Corporate Credit Card Expenses.

        Parameters:
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list.
            (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            spent_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            state(str): A parameter to filter expenses by the state that they're in. (optional)
            reimbursement_state(str): A parameter to filter expenses by the state of reimbursement that they're in.
            (optional)
            personal(bool): A parameter to filter personal or company. (optional)
            transaction_type(str): A parameter to filter expenses by transaction type DEBIT/CREDIT. (optional)
            settlement_id(str): List of settlement ids.
            exported (bool): If set to true, all expenses that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Corporate Credit Card Expenses schema.
        """
        return self._get_request({
            'limit': limit,
            'offset': offset,
            'updated_at': updated_at,
            'spent_at': spent_at,
            'exported': exported,
            'personal': personal,
            'state': state,
            'transaction_type': transaction_type,
            'settlement_id': settlement_id,
            'reimbursement_state': reimbursement_state
        }, CorporateCreditCardExpenses.GET_CORPORATE_CREDIT_CARD_EXPENSES)

    def count(self, updated_at=None, spent_at=None, exported=None, personal=None, state=None, transaction_type=None,
              settlement_id=None, reimbursement_state=None):
        """Get a count of all Corporate Credit Card Expenses.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            spent_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            state(str): A parameter to filter expenses by the state that they're in. (optional)
            reimbursement_state(str): A parameter to filter expenses by the state of reimbursement that they're in.
            (optional)
            personal(bool): A parameter to filter personal or company. (optional)
            transaction_type(str): A parameter to filter expenses by transaction type DEBIT/CREDIT. (optional)
            settlement_id(str): List of settlement ids.
            exported (bool): If set to true, all expenses that are exported alone will be returned. (optional)

        Returns:
            Integer with count.
        """
        return self._get_request({
            'updated_at': updated_at,
            'spent_at': spent_at,
            'exported': exported,
            'personal': personal,
            'state': state,
            'transaction_type': transaction_type,
            'settlement_id': settlement_id,
            'reimbursement_state': reimbursement_state
        }, CorporateCreditCardExpenses.GET_CORPORATE_CREDIT_CARD_EXPENSES_COUNT)

    def get_all(self, updated_at=None, spent_at=None, exported=None, personal=None, state=None, transaction_type=None,
                settlement_id=None, reimbursement_state=None):
        """
        Get all the corporate credit card expenses based on paginated call
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            spent_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            state(str): A parameter to filter expenses by the state that they're in. (optional)
            reimbursement_state(str): A parameter to filter expenses by the state of reimbursement that they're in.
            (optional)
            personal(bool): A parameter to filter personal or company. (optional)
            transaction_type(str): A parameter to filter expenses by transaction type DEBIT/CREDIT. (optional)
            settlement_id(str): List of settlement ids.
            exported (bool): If set to true, all expenses that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Corporate Credit Card Expenses schema.
        """
        ccc_expenses = []

        if settlement_id and len(settlement_id) > 40:
            pages = range(0, len(settlement_id), 40)
            chunks = []

            for i in range(0, len(pages)-1):
                chunks.append(settlement_id[pages[i]:pages[i+1]])
            chunks.append(settlement_id[pages[len(pages)-1]:])

            for chunk in chunks:
                count = self.count(settlement_id=chunk, updated_at=updated_at, spent_at=spent_at,
                                   exported=exported, personal=personal, transaction_type=transaction_type,
                                   state=state, reimbursement_state=reimbursement_state)['count']
                page_size = 300
                for i in range(0, count, page_size):
                    segment = self.get(
                        offset=i, limit=page_size, settlement_id=chunk, updated_at=updated_at, spent_at=spent_at,
                        exported=exported, personal=personal, transaction_type=transaction_type, state=state,
                        reimbursement_state=reimbursement_state
                    )
                    ccc_expenses = ccc_expenses + segment['data']
            return ccc_expenses

        count = self.count(settlement_id=settlement_id, updated_at=updated_at, spent_at=spent_at,
                           exported=exported, personal=personal, transaction_type=transaction_type,
                           state=state, reimbursement_state=reimbursement_state)['count']
        page_size = 300
        for i in range(0, count, page_size):
            segment = self.get(
                offset=i, limit=page_size, settlement_id=settlement_id, updated_at=updated_at, spent_at=spent_at,
                exported=exported, personal=personal, transaction_type=transaction_type, state=state,
                reimbursement_state=reimbursement_state
            )
            ccc_expenses = ccc_expenses + segment['data']
        return ccc_expenses
