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
