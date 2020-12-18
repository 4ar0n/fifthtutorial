
import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account


import csv
import requests
from pprint import pprint
from datetime import datetime , timedelta

cred_path = "/Users/aaronlee/Downloads/my-project-20190202-7af09df97e06.json"

def write_sheet_data(spreadsheet_id , sheetname ,  data):
    try:
        scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
        secret_file = cred_path

        credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
        service = discovery.build('sheets', 'v4', credentials=credentials)
        
        range_ = sheetname  # TODO: Update placeholder value.

        value_input_option = "USER_ENTERED"  # TODO: Update placeholder value.

        value_range_body = {'values': data}

        

        request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()


    except OSError as e:
        print (e)


def import_csv_url(CSV_URL):

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

    for row in my_list:
        for key, val in row.items():
            try:
                row[key] = int(val)
            except:
                pass
    return my_list



def turn_list_to_dict(key,data):
    dict={}
    for row in data:
        dict[row[key]]=row
    return dict



ac_type_db = [  {"id":1,"category":"Assets"},
                {"id":2,"category":"Liabilities"},
                {"id":3,"category":"Capitals"},
                {"id":4,"category":"Revenues"},
                {"id":5,"category":"Expenses"},
            ]

ac_db =     [   {"id":1,"category":1,"account":"Bank"},
                 {"id":2,"category":3,"account":"Aaron's Capital"},
                 {"id":4,"category":4,"account":"Tuition Income"},
                 {"id":5,"category":2,"account":"Loan from Billy"},
                 {"id":6,"category":5,"account":"Rental Expenses"},
                 {"id":7,"category":1,"account":"Furnitures"},
                 {"id":8,"category":5,"account":"Salaries"},
                 {"id":9,"category":1,"account":"Cash"},
                 {"id":12,"category":5,"account":"Printing Expenses"},
                 {"id":13,"category":5,"account":"Stationery"},
                 {"id":14,"category":4,"account":"Government Subsidy"},
             ]

branch_db =     [   {"id":1,"branch":"Prince Edward"},
                    {"id":2,"branch":"Causeway Bay"},
                ]











