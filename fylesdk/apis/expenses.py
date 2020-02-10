from .api_base import ApiBase


class Expenses(ApiBase):
    """Class for Expenses APIs."""

    POST_EXPENSE = '/api/tpa/v1/expenses'
    GET_EXPENSES = '/api/tpa/v1/expenses'
    GET_EXPENSES_COUNT = '/api/tpa/v1/expenses/count'
    GET_EXPENSE_BY_ID = '/api/tpa/v1/expenses/{0}'
    GET_EXPENSE_ATTACHMENTS = '/api/tpa/v1/expenses/{0}/attachments'

    def post(self, data):
        """Create an Expense for an Employee.

        Parameters:
            data (dict): Dict in Expense schema.
        
        Returns:
            ID from the new Expense.
        """
        return self._post_request(data, Expenses.POST_EXPENSE)

    def get(self, updated_at=None, settled_at=None, reimbursed_at=None, approved_at=None, state=None, offset=None,
            verified=None, limit=None, fund_source=None, settlement_id=None, exported=None, spent_at=None,
            report_id=None):
        """Get a list of existing Expenses, excluding the file attachments, that match the parameters.
        
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list.
            (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            reimbursed_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            state(str): A parameter to filter expenses by the state that they're in. (optional)
            verified(bool): A parameter to filter verified or unverified expenses. (optional)
            fund_source(str): A parameter to filter expenses by fund source. (optional)
            settlement_id(str): List of settlement ids.
            exported (bool): If set to true, all Settlements that are exported alone will be returned. (optional)
            spent_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            report_id(str): List of report ids.

        Returns:
            List with dicts in Expenses schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'settled_at': settled_at,
            'reimbursed_at': reimbursed_at,
            'approved_at': approved_at,
            'state': state,
            'verified': verified,
            'fund_source': fund_source,
            'settlement_id': settlement_id,
            'exported': exported,
            'spent_at': spent_at,
            'report_id': report_id
        }, Expenses.GET_EXPENSES)

    def count(self, updated_at=None, settled_at=None, reimbursed_at=None, approved_at=None, state=None,
              verified=None, fund_source=None, settlement_id=None, exported=None, spent_at=None, report_id=None):
        """Get the count of existing Expenses that match the given parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            reimbursed_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            state(str): A parameter to filter expenses by the state that they're in. (optional)
            verified(bool): A parameter to filter verified or unverified expenses. (optional)
            fund_source(str): A parameter to filter expenses by fund source. (optional)
            settlement_id(str): List of settlement ids.
            exported (bool): If set to true, all Settlements that are exported alone will be returned. (optional)
            spent_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            report_id(str): List of report ids.

        Returns:
            Count of Expenses.
        """
        return self._get_request({
            'updated_at': updated_at,
            'settled_at': settled_at,
            'reimbursed_at': reimbursed_at,
            'approved_at': approved_at,
            'state': state,
            'verified': verified,
            'fund_source': fund_source,
            'settlement_id': settlement_id,
            'exported': exported,
            'spent_at': spent_at,
            'report_id': report_id
        }, Expenses.GET_EXPENSES_COUNT)

    def get_by_id(self, expense_id):
        """Get an Expense by Id including the file attachments.

        Parameters:
            expense_id (str): Unique ID to find an Expense. Expense Id is our internal Id, it starts with prefix tx always.(required)

        Returns:
            Dict in Expense schema.
        """
        return self._get_request({}, Expenses.GET_EXPENSE_BY_ID.format(expense_id))

    def get_all(self, settlement_id=None, updated_at=None, settled_at=None, reimbursed_at=None, approved_at=None,
                state=None, verified=None, fund_source=None, exported=None, spent_at=None, report_id=None):
        """
        Get all the Expenses based on paginated call
        """
        expenses = []

        if (settlement_id and len(settlement_id) > 20) and (report_id and len(report_id) > 20):
            settlement_pages = range(0, len(settlement_id), 40)
            settlement_chunks = []
            report_pages = range(0, len(report_id), 40)
            report_chunks = []

            for i in range(0, len(settlement_pages)-1):
                settlement_chunks.append(settlement_id[settlement_pages[i]:settlement_pages[i+1]])
            settlement_chunks.append(settlement_id[settlement_pages[len(settlement_pages)-1]:])

            for i in range(0, len(report_pages)-1):
                report_chunks.append(report_id[report_pages[i]:report_pages[i+1]])
            report_chunks.append(report_id[report_pages[len(report_pages)-1]:])

            for settlement_chunk, report_chunk in zip(settlement_chunks, report_chunks):
                count = self.count(settlement_id=settlement_chunk, updated_at=updated_at, settled_at=settled_at,
                                   reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                                   verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=report_chunk)['count']
                page_size = 300
                for i in range(0, count, page_size):
                    segment = self.get(
                        offset=i, limit=page_size, settlement_id=settlement_chunk, updated_at=updated_at,
                        settled_at=settled_at,
                        reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                        verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=report_chunk
                    )
                    expenses = expenses + segment['data']
            return expenses

        if settlement_id and len(settlement_id) > 40:
            pages = range(0, len(settlement_id), 40)
            chunks = []

            for i in range(0, len(pages)-1):
                chunks.append(settlement_id[pages[i]:pages[i+1]])
            chunks.append(settlement_id[pages[len(pages)-1]:])

            for chunk in chunks:
                count = self.count(settlement_id=chunk, updated_at=updated_at, settled_at=settled_at,
                                   reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                                   verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=report_id)['count']
                page_size = 300
                for i in range(0, count, page_size):
                    segment = self.get(
                        offset=i, limit=page_size, settlement_id=chunk, updated_at=updated_at,
                        settled_at=settled_at,
                        reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                        verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=report_id
                    )
                    expenses = expenses + segment['data']
            return expenses

        if report_id and len(report_id) > 40:
            pages = range(0, len(report_id), 40)
            chunks = []

            for i in range(0, len(pages)-1):
                chunks.append(report_id[pages[i]:pages[i+1]])
            chunks.append(report_id[pages[len(pages)-1]:])

            for chunk in chunks:
                count = self.count(settlement_id=settlement_id, updated_at=updated_at, settled_at=settled_at,
                                   reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                                   verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=chunk)['count']
                page_size = 300
                for i in range(0, count, page_size):
                    segment = self.get(
                        offset=i, limit=page_size, settlement_id=settlement_id, updated_at=updated_at,
                        settled_at=settled_at,
                        reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                        verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=chunk
                    )
                    expenses = expenses + segment['data']
            return expenses

        count = self.count(settlement_id=settlement_id, updated_at=updated_at, settled_at=settled_at,
                           reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                           verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=report_id)['count']
        page_size = 300
        for i in range(0, count, page_size):
            segment = self.get(
                offset=i, limit=page_size, settlement_id=settlement_id, updated_at=updated_at, settled_at=settled_at,
                reimbursed_at=reimbursed_at, approved_at=approved_at, state=state,
                verified=verified, fund_source=fund_source, exported=exported, spent_at=spent_at, report_id=report_id
            )
            expenses = expenses + segment['data']
        return expenses

    def get_attachments(self, expense_id):
        """Get all the file attachments associated with an Expense.

        Parameters:
            expense_id (str): Unique ID to find an Expense. Expense Id is our internal Id, it starts with preifx tx always. (required)

        Returns:
            List with dicts in Attachments schema.
        """
        return self._get_request({}, Expenses.GET_EXPENSE_ATTACHMENTS.format(expense_id))
