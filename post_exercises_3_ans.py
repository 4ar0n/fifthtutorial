import random
from pprint import pprint
from datetime import datetime
import csv
import requests

ac_type_db = [  {"id":1,"category":"Asset"},
				 {"id":2,"category":"Liability"},
				 {"id":3,"category":"Capital"},
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

    return my_list

def interpret_csv(biz_data_raw):

    for i in biz_data_raw:

        for j in branch_db:
            if str(j["id"]) == str(i["branch"]):
                i["branch"] = j["branch"]

        for h in ac_db:
            if str(h["id"]) == str(i["credit"]):
                i["credit"] = h["account"]
                for k in ac_type_db:
                    if k["id"] == h["category"]:
                        i["cr_acct_type"] = k["category"]
            if str(h["id"]) == str(i["debit"]):
                i["debit"] = h["account"]
                for k in ac_type_db:
                    if k["id"] == h["category"]:
                        i["db_acct_type"] = k["category"]

    return biz_data_raw

def interpret_csv_aar(biz_data_raw):
    for tran in biz_data_raw:
        trans['debit'] = trans['debit'] 
path = 'https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/post_exercises_3_db.csv'
biz_data_raw = import_csv_url(path)
biz_data_dict=interpret_csv(biz_data_raw)

pprint (biz_data_dict)
