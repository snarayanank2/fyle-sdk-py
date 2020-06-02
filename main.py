from fylesdk import FyleSDK
import csv
import datetime
import base64

print('establishing connection ', datetime.datetime.now())
connection = FyleSDK(
    base_url='https://accounts.staging.fyle.in',
    client_id='tpaDp1OcAAYRa',
    client_secret='ujc3iWI2g9',
    refresh_token='eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTA2NTgzMjQsImlzcyI6IkZ5bGVBcHAiLCJvcmdfdXNlcl9pZCI6Ilwib3VGa08yaUFnWjNyXCIiLCJ0cGFfaWQiOiJcInRwYURwMU9jQUFZUmFcIiIsInRwYV9uYW1lIjoiXCJBc2h3aW4gVGVzdFwiIiwiY2x1c3Rlcl9kb21haW4iOiJcImh0dHBzOi8vc3RhZ2luZy5meWxlLmluXCIiLCJleHAiOjE5MDYwMTgzMjR9.-aAmrDV85B0nEzEHk428Jecd6zxddrcpPT_4LA_bGuc',
    jobs_url=''
)
print('got connected ', datetime.datetime.now())

def getEmployees():
    print('get emp ', datetime.datetime.now())
    response = connection.Employees.get()
    print('got emp ', datetime.datetime.now())

    # print(response["data"])
    fields = ['id', 'approver1_email', 'user_id', 'employee_email', 'created_at', 'full_name']
    filename = "getEmployees.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for key in response['data']:
            csvwriter.writerow([key['id'], key['approver1_email'], key['user_id'], key['employee_email'], key['created_at'], key['full_name']])

def getExpense():
    response = connection.Expenses.get()

    fields = ['id', 'source', 'employee_id', 'employee_email', 'spent_at', 'currency']
    filename = "getExpense.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for key in response['data']:
            csvwriter.writerow([key['id'], key['source'], key['employee_id'], key['employee_email'], key['spent_at'], ['currency']])

def getFile():
    response = connection.Expenses.get_attachments(expense_id='txsG7L25bCrv')
    imgdata = base64.b64decode(response['data'][0]['content'])
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

def postFile():
    # response = connection.Files.post('/home/ashwin/fyle/fyle-sdk-py/some_image.jpg')
    # print(response)
    response = connection.Files.create_upload_url(file_id='fi23HxWdEU5t')
    print(response)
    response = connection.Files.create_download_url(file_id='fi23HxWdEU5t')
    print(response)

# getExpense()
# getEmployees()
# getFile()
