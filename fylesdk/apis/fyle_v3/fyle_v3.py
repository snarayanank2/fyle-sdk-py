"""
Fyle V3 APIs Base Class
"""
from .expenses import Expenses
from .reports import Reports
from .employees import Employees
from .orgs import Orgs
from .reimbursements import Reimbursements
from .cost_centes import CostCenters
from .categories import Categories
from .projects import Projects
from .refunds import Refunds
from .balance_transfers import BalanceTransfers
from .settlements import Settlements
from .advance_requests import AdvanceRequests
from .advances import Advances
from .bank_transactions import BankTransactions
from .trip_requests import TripRequests
from .expense_custom_properties import ExpenseCustomProperties
from .employee_custom_properties import EmployeeCustomProperties
from .advance_request_custom_properties import AdvanceRequestCustomProperties
from .trip_request_custom_properties import TripRequestCustomProperties


class FyleV3:
    def __init__(self):
        """
        Constructor to Initialize all APIs
        """
        # Initialize V3 API Classes
        self.expenses = Expenses()
        self.reports = Reports()
        self.employees = Employees()
        self.orgs = Orgs()
        self.reimbursements = Reimbursements()
        self.cost_centers = CostCenters()
        self.categories = Categories()
        self.projects = Projects()
        self.refunds = Refunds()
        self.balance_transfers = BalanceTransfers()
        self.settlements = Settlements()
        self.advance_requests = AdvanceRequests()
        self.advances = Advances()
        self.bank_transactions = BankTransactions()
        self.trip_requests = TripRequests()
        self.expense_custom_properties = ExpenseCustomProperties()
        self.employee_custom_properties = EmployeeCustomProperties()
        self.advance_request_custom_properties = AdvanceRequestCustomProperties()
        self.trip_request_custom_properties = TripRequestCustomProperties()
