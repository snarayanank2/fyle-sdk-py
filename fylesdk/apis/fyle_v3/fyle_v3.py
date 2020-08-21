"""
Fyle V3 APIs Base Class
"""
from .expenses import Expenses
from .employees import Employees
from .orgs import Orgs
from .reimbursements import Reimbursements
from .cost_centes import CostCenters


class FyleV3:
    def __init__(self):
        """
        Constructor
        """
        # Initialize V3 API Classes
        self.expenses = Expenses()
        self.employees = Employees()
        self.orgs = Orgs()
        self.reimbursements = Reimbursements()
        self.cost_centers = CostCenters()
