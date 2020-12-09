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

ac_type_db = [  {"id":1,"category":"Asset"},
                {"id":2,"category":"Liability"},
                {"id":3,"category":"Capital"},
                {"id":4,"category":"Revenues"},
                {"id":5,"category":"Expenses"},
            ]
ac_db =     [   {"id":1,"category":1,"account":"Bank"},
                {"id":2,"category":3,"account":"Aaron's Capital"},
                {"id":4,"category":4,"account":"Tuition Income"},
                {"id":4,"category":2,"account":"Loan from Billy"},
                {"id":5,"category":5,"account":"Rental Expenses"},
                {"id":6,"category":1,"account":"Furnitures"},
                {"id":7,"category":5,"account":"Salaries"},
                {"id":9,"category":1,"account":"Cash"},
                {"id":22,"category":5,"account":"Printing Expenses"},
                {"id":42,"category":5,"account":"Stationery"},
                {"id":53,"category":4,"account":"Government Subsidy"},
            ]

branch_db =     [   {"id":1,"branch":"Prince Edward"},
                    {"id":2,"branch":"Causeway Bay"},
                ]

