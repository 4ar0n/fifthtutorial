'''
Aaron is a tuition business owner with two centres at Prince Edward and Causeway bay respectively.
His accounting system database is a typical relational database that you the entry has to be looked up to other table to become meaningful.

The data for 2018 and 2019 are stored in post_exercises_3_db.csv

Requirement:
3.1 download / and output the post_exercises_3_db.csv AS dictionary and transalate them into a meaningful data eg:

{'amount': 8235, 'branch': 1,'credit': 9, 'date': '2019-11-4','debit': 42,'id': 4946}  ==>
{'amount': 8235, 'branch': "Prince Edward",'credit': Cash, 'date': '2019-11-4','debit': Stationery,'id': 4946} 

and then output to post_exercises_3_db2.csv

3.2
Produce an Income statement for the year of 2019
Where Income statement: REVENUES - EXPENSES = NET PROFIT
LIST ALL ITEMS with items and amount (do not list 0 items)

Produce a BALANCE SHEET  for the year of 2019
Where ASSETS (of all time)= LIABILITIES (of all time) + CAPITAL (of all time) + NET PROFIT (of 2019)
LIST ALL ITEMS with items and amount (do not list 0 items)

3.3
Produce a branch comparative income statement and balance sheet for comparasion between Causeway Bay and Prince Edward for 2018.
with the following format:
ITEMS Pince Edward , Causeway Bay

3.4
Procuce a year compartive balance sheet for comparasion between 2018 and 2019,% change is to be reported.
with the following format: ITEMS 2018, 2019 ,% change


'''

import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account

from pprint import pprint
cred_path = "/Users/aaronlee/Downloads/my-project-20190202-7af09df97e06.json"

def write_sheet_data(spreadsheet_id , sheetname ,  data):
    # REFERENCE https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate
    try:
        scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
        secret_file = cred_path

        credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
        service = discovery.build('sheets', 'v4', credentials=credentials)
        
        range_ = sheetname  # TODO: Update placeholder value.

        # How the input data should be interpreted.
        value_input_option = "USER_ENTERED"  # TODO: Update placeholder value.

        value_range_body = {'values': data}
            # TODO: Add desired entries to the request body. All existing entries
            # will be replaced.
        

        request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()


        # TODO: Change code below to process the `response` dict:
        pprint(response)


    except OSError as e:
        print (e)

import csv
import requests
from pprint import pprint
from datetime import datetime , timedelta

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


ac_type_dict = turn_list_to_dict("id",ac_type_db)
ac_dict = turn_list_to_dict("id",ac_db)
branch_dict = turn_list_to_dict("id",branch_db)

path = 'https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/post_exercises_3_db.csv'

entries =  import_csv_url(path)

for i in range (0, len(entries)):
    entries[i]['cr_type'] = ac_type_dict[ac_dict[entries[i]['credit']]['category']]["category"]
    entries[i]['dr_type'] = ac_type_dict[ac_dict[entries[i]['debit']]['category']]["category"]
    entries[i]['cr_name'] = ac_dict[entries[i]['credit']]['account']
    entries[i]['dr_name'] = ac_dict[entries[i]['debit']]['account']
    entries[i]['branch_name'] = branch_dict[entries[i]['branch']]['branch']
    entries[i]['date'] = datetime.strptime(entries[i]['date'], "%Y-%m-%d")


# pprint (entries)

def cal_balance(ac_id ,entries, beg,end):
    balance = 0
    for entry in entries:
        if entry['date']>=beg and entry['date']<=end:
            if entry['debit'] == ac_id:
                balance+=entry['amount']
            if entry['credit'] == ac_id:
                balance-=entry['amount']
    return balance



def category_statement(cat_id , entries , beg, end):
    cat_list = [[ac_type_dict[cat_id]['category'].upper()]]
    for ac , acinfo in ac_dict.items():
        if acinfo["category"] == cat_id:
            ac_name = ac_dict[ac]['account']
            cat_list.append([ac_name, cal_balance(ac ,entries, beg,end)])
    return cat_list

def net_profit(revenues_list , expenses_list):
    netprofit = 0 
    for item in revenues_list:
        try:
            netprofit += item[1]
        except:
            pass

    for item in expenses_list:
        try:
            netprofit += item[1]
        except:
            pass

    return netprofit


opening =  datetime(1980,1,1,0,0)
end_2018 = datetime(2018,12,31,0,0)

beg_2019 = datetime(2019,1,1,0,0)
end_2019 = datetime(2019,12,31,0,0)

# print (cal_balance(1 ,entries, beg ,end_2019))

def financial_statements(beg,end):
    assets = category_statement(1,entries , opening , end)
    liabilities= category_statement(2,entries , opening , end)
    
    capital = category_statement(3,entries , opening , end)

    retained_revenues = category_statement(4,entries , opening , beg-timedelta(days=1))
    retained_expenses = category_statement(5,entries , opening , beg-timedelta(days=1))
    retained_profits = net_profit(retained_revenues , retained_expenses)

    revenues = category_statement(4,entries , beg , end)
    expenses = category_statement(5,entries , beg , end)
    netprofit = net_profit(revenues , expenses)

    capital += [["Retained Profits" , retained_profits]]
    capital += [["Net Profit" , netprofit]]


    balance_sheet  = [["Balance Sheet" , "as at "+end.strftime("%Y-%m-%d")]] + assets + liabilities + capital
    income_statement =  [["Income Statement" , "for the year ended " + end.strftime("%Y-%m-%d")]] +revenues + expenses + [["Net Profit" , netprofit]]

    return {"is":income_statement,"bs":balance_sheet}

fs_2019 = financial_statements(beg_2019,end_2019)
# pprint (fs_2019["is"])
# pprint (fs_2019["bs"])


spreadsheet_id="1PqiDuIRV8BuDAzcjFdH_z0HTWaP0sr7TCRdUpDIPrcU"
write_sheet_data(spreadsheet_id , "a1" , fs_2019["is"])
write_sheet_data(spreadsheet_id , "d1" , fs_2019["bs"])



























