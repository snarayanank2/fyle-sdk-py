from .utils import get_access_token
from .apis import *


class FyleSDK:
    """The main class which creates a connection with Fyle APIs using OAuth2 authentication (refresh token grant type).

    Parameters:
        client_id (str): Client ID for Fyle API.
        client_secret (str): Client secret for Fyle API.
        refresh_token (str): Refresh token for Fyle API.
    """

    def __init__(self, client_id, client_secret, refresh_token):
        # store the credentials
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token

        # create an object for each api
        self.Employees = Employees()
        self.Expenses = Expenses()
        self.Reports = Reports()
        self.Categories = Categories()
        self.Advances = Advances()
        self.Refunds = Refunds()
        self.Reimbursements = Reimbursements()
        self.CostCenters = CostCenters()
        self.Projects = Projects()
        self.BalanceTransfers = BalanceTransfers()
        self.Exports = Exports()
        self.TripRequests = TripRequests()
        self.TransportationRequests = TransportationRequests()
        self.TransportationBookings = TransportationBookings()
        self.TransportationBookingCancellations = TransportationBookingCancellations()
        self.HotelRequests = HotelRequests()
        self.HotelBookings = HotelBookings()
        self.HotelBookingCancellations = HotelBookingCancellations()

        # get the access token
        self.update_access_token()


    def update_access_token(self):
        """Update the access token and change it in all API objects."""
        
        access_token = get_access_token(self.__client_id, self.__client_secret, self.__refresh_token)
        
        self.Employees.change_access_token(access_token)
        self.Expenses.change_access_token(access_token)
        self.Reports.change_access_token(access_token)
        self.Categories.change_access_token(access_token)
        self.Advances.change_access_token(access_token)
        self.Refunds.change_access_token(access_token)
        self.Reimbursements.change_access_token(access_token)
        self.CostCenters.change_access_token(access_token)
        self.Projects.change_access_token(access_token)
        self.BalanceTransfers.change_access_token(access_token)
        self.Exports.change_access_token(access_token)
        self.TripRequests.change_access_token(access_token)
        self.TransportationRequests.change_access_token(access_token)
        self.TransportationBookings.change_access_token(access_token)
        self.TransportationBookingCancellations.change_access_token(access_token)
        self.HotelRequests.change_access_token(access_token)
        self.HotelBookings.change_access_token(access_token)
        self.HotelBookingCancellations.change_access_token(access_token)
