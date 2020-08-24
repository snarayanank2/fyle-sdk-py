# FyleSDK

Python SDK for accessing Fyle APIs. [Fyle](https://www.fylehq.com/) is an expense management system.

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).
        
        $ pip install fylesdk

## Usage

To use this SDK you'll need these Fyle credentials used for OAuth2 authentication: **client ID**, **client secret** and **refresh token**.

This SDK is very easy to use.
* First you'll need to create a connection using the main class FyleSDK.
```python
from fylesdk import FyleSDK

connection = FyleSDK(
    base_url='<YOUR BASE URL>',
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    refresh_token='<YOUR REFRESH TOKEN>'
)
```

* Introducing APIs version 3 from version 1.0.0 onwards. These are faster and more performant APIs but are still under development. To access them from the sdk do -
```python
# Transactions
expenses = connection.v3.expenses.get()
reports = connection.v3.reports.get()
advances = connection.v3.advances.get()
bank_transactions = connection.v3.bank_transactions.get()
refunds = connection.v3.refunds.get()

# Requests
advance_requests = connection.v3.advance_requests.get()
trip_requests = connection.v3.trip_requests.get()
reimbursements = connection.v3.reimbursements.get()
settlements = connection.v3.settlements.get()
balance_transfers = connection.v3.balance_transfers.get()

# Organisation Data
orgs = connection.v3.orgs.get()
employees = connection.v3.employees.get()
categories = connection.v3.categories.get()
projects = connection.v3.projects.get()
cost_centers = connection.v3.cost_centers.get()

# Custom Properties
advance_request_custom_properties = connection.v3.advance_request_custom_properties.get()
trip_request_custom_properties = connection.v3.trip_request_custom_properties.get()
employee_custom_properties = connection.v3.employee_custom_properties.get()
expense_custom_properties = connection.v3.expense_custom_properties.get()
```

*  After that you'll be able to access any of the 18 API classes.
```python
"""
USAGE: <FyleSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Get a list of all Employees (with all available details for Employee)
response = connection.Employees.get()

# Get count of Reports updated on or after 2019-01-01
response = connection.Reports.count(updated_at='gte:2019-01-01T00:00:00.000Z')

# Create a new Expense of 10 USD, spent at 2019-01-01 and from employee with email user@mail.com
new_expense = [{
    'employee_email': 'user@mail.com',
    'currency': 'USD',
    'amount': 10,
    'spent_at': '2019-01-01T00:00:00.000Z',
    'reimbursable': True
}]
response = connection.Expenses.post(new_expense)

```

You can also access fyle-jobs using this SDK.

First you'll need to create a connection using the main class FyleSDK with jobs_url.
```python
from fylesdk import FyleSDK

connection = FyleSDK(
    base_url='<YOUR BASE URL>',
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    refresh_token='<YOUR REFRESH TOKEN>',
    jobs_url='<FYLE JOBS URL>'
)
```
1. After that you'll be able to access *Jobs* API class
```python
"""
USAGE: <FyleSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""
# Trigger callback immediately
response = connection.Jobs.trigger_now(
                callback_url='callback_url',
                callback_method='POST', object_id='SDK1234', payload={
                    'ping': 'pong'
                },
                job_description='Trigger Now',
                org_user_id=org_user_id
)

# Trigger callback on Interval
response = connection.Jobs.trigger_interval(
                callback_url='callback_url',
                callback_method='POST', object_id='SDK1234', payload={
                    'ping': 'pong'
                },
                job_description='Trigger Now',
                org_user_id=org_user_id,
                start_datetime='yyyy-MM-ddTHH:mm:ss.SSSZ',
                hours='1'
)
```

See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
