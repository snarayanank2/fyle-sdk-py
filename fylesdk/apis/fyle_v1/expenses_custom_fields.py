from ..api_base import ApiBase

class ExpensesCustomFields(ApiBase):
    """Class for Expenses Custom Fields APIs."""

    GET_EXPENSES_CUSTOM_FIELDS = '/api/tpa/v1/expenses_custom_fields'

    def get(self, active=None):
        """Get a list of expenses input field matching the parameters.

        Parameters:
            active (boolean): To get the active fields only (optional)

        Returns:
            List with dicts in ExpenseCustomFields schema.
        """
        return self._get_request({
            'active': active
        }, ExpensesCustomFields.GET_EXPENSES_CUSTOM_FIELDS)