'''
Aaron is a tuition business owner with two centres at Prince Edward and Causeway bay respectively.
His accounting system database is a typical relational database that you the entry has to be looked up to other table to become meaningful.
The data for 2018 and 2019 are stored in post_exercises_3_db.csv
Requirement:
3.1 download / and output the post_exercises_3_db.csv AS dictionary and transalate them into a meaningful data eg:
{'amount': 8235, 'branch': 1,'credit': 9, 'date': '2019-11-4','debit': 42,'id': 4946}  ==>
{'amount': 8235, 'branch': "Prince Edward",'credit': Cash, 'date': '2019-11-4','debit': Stationery,'id': 4946} 
and then output to post_exercises_3_db2.csv

'''

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

cr_plus = ["Revenues", "Liability", "Capital"]
db_plus = ["Expenses", "Asset"]


import csv
import requests
from pprint import pprint

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

path = 'https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/post_exercises_3_db.csv'
biz_data_raw = import_csv_url(path)
biz_data_dict=interpret_csv(biz_data_raw)

# pprint(biz_data_dict)

'''
3.2
Produce an Income statement for the year of 2019
Where Income statement: REVENUES - EXPENSES = NET PROFIT
LIST ALL ITEMS with items and amount (do not list 0 items)
Produce a BALANCE SHEET  for the year of 2019
Where ASSETS (of all time)= LIABILITIES (of all time) + CAPITAL (of all time) + NET PROFIT (of 2019)
LIST ALL ITEMS with items and amount (do not list 0 items)

'''

from datetime import datetime

def income_summary(biz_data_dict, year_period, branch):

    summary = {}
    for i in ac_type_db:
        summary[i["category"]] =0

    for i in biz_data_dict:

        if year_period[0] <= datetime.strptime(i["date"], "%Y-%m-%d") <= year_period[1] and i["branch"] in branch:  

            if i["cr_acct_type"] in cr_plus:
                summary[i["cr_acct_type"]]+=int(i["amount"])
            else:
                summary[i["cr_acct_type"]]-=int(i["amount"])

            if i["db_acct_type"] in db_plus:
                summary[i["db_acct_type"]]+=int(i["amount"])
            else:
                summary[i["db_acct_type"]]-=int(i["amount"])    

    summary["Check"] = 0
    for k, v in summary.items():
        if k in db_plus:
            summary["Check"]+=v
        else:
            summary["Check"]-=v
    return summary

# pprint(income_summary(biz_data_dict, [datetime(2018, 1, 1),datetime(2019, 12, 31)], ["Prince Edward", "Causeway Bay"]))

def income_statement(biz_data_dict, year_period, branch):

    summary = {}
    summary["Net Profit"] = 0
    for i in ac_db:
        if i["category"] in [4,5]:
            summary[i["account"]] =0

    for i in biz_data_dict:

        if year_period[0] <= datetime.strptime(i["date"], "%Y-%m-%d") <= year_period[1] and i["branch"] in branch:  

            if i["cr_acct_type"] == "Revenues":
                summary[i["credit"]]+=int(i["amount"])
            elif i["cr_acct_type"] == "Expenses":
                summary[i["credit"]]-=int(i["amount"])


            if i["db_acct_type"] == "Revenues":
                summary[i["debit"]]-=int(i["amount"])
            elif i["db_acct_type"] == "Expenses":
                summary[i["debit"]]+=int(i["amount"])

    
    for i in ac_db:
        if i["category"] in [4]:
            summary["Net Profit"]+=summary[i["account"]]
        elif i["category"] in [5]:
            summary["Net Profit"]-=summary[i["account"]]

    return summary

# pprint(income_statement(biz_data_dict, [datetime(2019, 1, 1),datetime(2019, 12, 31)], ["Prince Edward", "Causeway Bay"]))

def balance_sheet(biz_data_dict, year_period, branch):

    summary = {}
    summary["Check"] = 0
    for i in ac_db:
        if i["category"] in [1,2,3]:
            summary[i["account"]] = 0

    for i in biz_data_dict:

        if year_period[0] <= datetime.strptime(i["date"], "%Y-%m-%d") <= year_period[1] and i["branch"] in branch:  

            if i["cr_acct_type"] in ["Asset"]:
                summary[i["credit"]]-=int(i["amount"])
            elif i["cr_acct_type"] in ["Liability", "Capital"]:
                summary[i["credit"]]+=int(i["amount"])

            if i["db_acct_type"] in ["Asset"]:
                summary[i["debit"]]+=int(i["amount"])
            elif i["db_acct_type"] in ["Liability", "Capital"]:
                summary[i["debit"]]-=int(i["amount"])

    summary["Aaron's Capital"]+=income_statement(biz_data_dict, year_period, branch)["Net Profit"]
    
    for i in ac_db:
        if i["category"] in [1]:
            summary["Check"]+=summary[i["account"]]
        elif i["category"] in [2,3]:
            summary["Check"]-=summary[i["account"]]

    return summary

pprint(balance_sheet(biz_data_dict, [datetime(2019, 1, 1),datetime(2019, 12, 31)], ["Prince Edward", "Causeway Bay"]))


'''
3.3
Produce a branch comparative income statement and balance sheet for comparasion between Causeway Bay and Prince Edward for 2018.
with the following format:
ITEMS Pince Edward , Causeway Bay
'''
def income_comparison(year_period, branch, comparison_factor):

    Headings = ["ITEMS"]
    Income_list =[]

    if comparison_factor == "branch":
        for i in branch:
            Income_list.append(income_statement(biz_data_dict,year_period,i))
            Headings.append(i)

    if comparison_factor == "year":
        for i in year_period:
            Income_list.append(income_statement(biz_data_dict,i,branch))
            Headings.append(i)


    Overall_Income = [Headings]

    for k, v in Income_list[0].items():
        tmp_entry =[]
        tmp_entry.append(k)
        tmp_entry.append(v)
        for g in range (1, len(Income_list)):
            tmp_entry.append(Income_list[g][k])
        Overall_Income.append(tmp_entry)

    return Overall_Income

income_comparison = income_comparison([[datetime(2018, 1, 1),datetime(2018, 12, 31)], [datetime(2019, 1, 1),datetime(2019, 12, 31)]], ["Prince Edward", "Causeway Bay"], "year")
# income_comparison = income_comparison([datetime(2018, 1, 1),datetime(2018, 12, 31)], ["Prince Edward", "Causeway Bay"], "branch")
pprint(income_comparison)

'''
3.4
Procuce a year compartive balance sheet for comparasion between 2018 and 2019,% change is to be reported.
with the following format: ITEMS 2018, 2019 ,% change
'''


def bs_comparison(year_period, branch, comparison_factor):

    Headings = ["ITEMS"]
    BS_list =[]

    if comparison_factor == "branch":
        for i in branch:
            BS_list.append(balance_sheet(biz_data_dict,year_period,i))
            Headings.append(i)

    if comparison_factor == "year":
        BS_list.append(balance_sheet(biz_data_dict,year_period[0],branch))
        Headings.append(year_period[0])
        
        for i in range(1, len(year_period)):
            BS_list.append(balance_sheet(biz_data_dict,year_period[i],branch))
            Headings.append(year_period[i])
            Headings.append("YoY Chg")


    Overall_BS = [Headings]

    for k, v in BS_list[0].items():
        tmp_entry =[]
        tmp_entry.append(k)
        tmp_entry.append(v)
        # tmp_entry.append("N/A")
        for g in range (1, len(BS_list)):
            tmp_entry.append(BS_list[g][k])
            if BS_list[g-1][k] == 0:
                tmp_entry.append("N/A")
            else:
                tmp_entry.append("{:.2%}".format(BS_list[g][k]/BS_list[g-1][k] - 1))
        Overall_BS.append(tmp_entry)

    return Overall_BS

BS_comparison = bs_comparison([[datetime(2018, 1, 1),datetime(2018, 12, 31)], [datetime(2019, 1, 1),datetime(2019, 12, 31)]], ["Prince Edward", "Causeway Bay"], "year")
pprint(BS_comparison)
