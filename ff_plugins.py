
import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account


import csv
import requests
from pprint import pprint
from datetime import datetime , timedelta
from pprint import pprint
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

        pprint (response)

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














