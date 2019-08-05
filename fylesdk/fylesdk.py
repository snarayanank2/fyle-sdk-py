from .exceptions import *
from .apis import *
import requests
import json


class FyleSDK:
    """The main class which creates a connection with Fyle APIs using OAuth2 authentication (refresh token grant type).

    Parameters:
        client_id (str): Client ID for Fyle API.
        client_secret (str): Client secret for Fyle API.
        refresh_token (str): Refresh token for Fyle API.
    """

    TOKEN_URL = '{}/api/oauth/token'

    def __init__(self, base_url, client_id, client_secret, refresh_token):
        # store the credentials
        self.__base_url = base_url
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
        self.Settlements = Settlements()
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
        self.BankTransactions = BankTransactions()
        self.Files = Files()

        # get the access token
        self.update_access_token()
        self.set_server_url()


    def update_access_token(self):
        """Update the access token and change it in all API objects."""
        
        access_token = self.__get_access_token()
        
        self.Employees.change_access_token(access_token)
        self.Expenses.change_access_token(access_token)
        self.Reports.change_access_token(access_token)
        self.Categories.change_access_token(access_token)
        self.Advances.change_access_token(access_token)
        self.Refunds.change_access_token(access_token)
        self.Reimbursements.change_access_token(access_token)
        self.Settlements.change_access_token(access_token)
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
        self.BankTransactions.change_access_token(access_token)
        self.Files.change_access_token(access_token)

    
    def set_server_url(self):
        """Update the access token and change it in all API objects."""
        
        base_url = self.__base_url
        
        self.Employees.set_server_url(base_url)
        self.Expenses.set_server_url(base_url)
        self.Reports.set_server_url(base_url)
        self.Categories.set_server_url(base_url)
        self.Advances.set_server_url(base_url)
        self.Refunds.set_server_url(base_url)
        self.Reimbursements.set_server_url(base_url)
        self.Settlements.set_server_url(base_url)
        self.CostCenters.set_server_url(base_url)
        self.Projects.set_server_url(base_url)
        self.BalanceTransfers.set_server_url(base_url)
        self.Exports.set_server_url(base_url)
        self.TripRequests.set_server_url(base_url)
        self.TransportationRequests.set_server_url(base_url)
        self.TransportationBookings.set_server_url(base_url)
        self.TransportationBookingCancellations.set_server_url(base_url)
        self.HotelRequests.set_server_url(base_url)
        self.HotelBookings.set_server_url(base_url)
        self.HotelBookingCancellations.set_server_url(base_url)
        self.BankTransactions.set_server_url(base_url)
        self.Files.set_server_url(base_url)



    def __get_access_token(self):
        """Get the access token using a HTTP post.
        
        Returns:
            A new access token.
        """

        api_data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token,
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }
        
        token_url = FyleSDK.TOKEN_URL.format(self.__base_url)
        response = requests.post(token_url, data=api_data)

        if response.status_code == 200:
            access_token = json.loads(response.text)['access_token']
            return access_token
        
        elif response.status_code == 401:
            raise UnauthorizedClientError('Wrong client secret or/and refresh token', response.text)

        elif response.status_code == 404:
            raise NotFoundClientError('Client ID doesn\'t exist', response.text)

        elif response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        else:
            raise FyleSDKError('Error: {0}'.format(response.status_code), response.text)