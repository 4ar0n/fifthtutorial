import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account

from pprint import pprint
cred_path = "/Users/aaronlee/Downloads/my-project-20190202-7af09df97e06.json"

def get_sheet_data(spreadsheet_id , range_name):
    
    try:
        scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
        secret_file = cred_path

        credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
        service = discovery.build('sheets', 'v4', credentials=credentials)
        

        result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
        numRows = result.get('values') if result.get('values')is not None else 0
        #print('{0} rows retrieved.'.format(numRows))

        return numRows
    except OSError as e:
        print (e)

spid="1PqiDuIRV8BuDAzcjFdH_z0HTWaP0sr7TCRdUpDIPrcU"
pprint (get_sheet_data(spid, "A:Z"))
