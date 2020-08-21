"""
Fyle V3 APIs Base Class
"""
from .expenses import Expenses
from .employees import Employees


class FyleV3:
    def __init__(self):
        """
        Constructor
        """
        # Initialize V3 API Classes
        self.expenses = Expenses()
        self.employees = Employees()
