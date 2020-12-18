from pprint import pprint
from datetime import datetime , timedelta
from ff_plugins import write_sheet_data , import_csv_url , turn_list_to_dict

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




''' I would rather turn those list into a dictionary, so that I dun need a loop to get its value, but directly assessing them so that my codes are cleaner and shorter and easier for reading. This is important because it not only enables collaborations, but also maintenance, debugging and further development.
'''
ac_type_dict = turn_list_to_dict("id",ac_type_db)
ac_dict = turn_list_to_dict("id",ac_db)
branch_dict = turn_list_to_dict("id",branch_db)

path = 'https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/post_exercises_3_db.csv'
entries =  import_csv_url(path)



'''
entries are made.
'''
for i in range (0, len(entries)):
    entries[i]['cr_type'] = ac_type_dict[ac_dict[entries[i]['credit']]['category']]["category"]
    entries[i]['dr_type'] = ac_type_dict[ac_dict[entries[i]['debit']]['category']]["category"]
    entries[i]['cr_name'] = ac_dict[entries[i]['credit']]['account']
    entries[i]['dr_name'] = ac_dict[entries[i]['debit']]['account']
    entries[i]['branch_name'] = branch_dict[entries[i]['branch']]['branch']
    entries[i]['date'] = datetime.strptime(entries[i]['date'], "%Y-%m-%d")






def cal_balance(ac_id ,entries, beg,end):
    balance = 0
    for entry in entries:
        if entry['date']>=beg and entry['date']<=end:
            if entry['debit'] == ac_id:
                balance+=entry['amount']
            if entry['credit'] == ac_id:
                balance-=entry['amount']
    return balance


'''
To automatically generate statement accounting to its type
'''
def category_statement(cat_id , entries , beg, end):
    cat_list = [[ac_type_dict[cat_id]['category'].upper()]]
    for ac , acinfo in ac_dict.items():
        if acinfo["category"] == cat_id:
            ac_name = ac_dict[ac]['account']
            cat_list.append([ac_name, cal_balance(ac ,entries, beg,end)])
    return cat_list

'''
A function just to calculate the net profit, as long as u supply with revenues and expenses list from the category_statement()
'''
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



def financial_statements(beg,end):
    assets = category_statement(1,entries , opening , end)
    liabilities= category_statement(2,entries , opening , end)
    
    capital = category_statement(3,entries , opening , end)


    '''
    This is how I manage to get the retained profits instead of gernating the balance sheets. Simple and beautiful.
    '''
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





opening =  datetime(1980,1,1,0,0)
end_2018 = datetime(2018,12,31,0,0)

beg_2019 = datetime(2019,1,1,0,0)
end_2019 = datetime(2019,12,31,0,0)
fs_2019 = financial_statements(beg_2019,end_2019)


spreadsheet_id="1PqiDuIRV8BuDAzcjFdH_z0HTWaP0sr7TCRdUpDIPrcU"
write_sheet_data(spreadsheet_id , "a1" , fs_2019["is"])
write_sheet_data(spreadsheet_id , "d1" , fs_2019["bs"])



























