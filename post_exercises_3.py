import random
from pprint import pprint
from datetime import datetime
import csv

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

accs = []
for ac in ac_db:
    accs.append(ac['id'])
pprint (accs)


transactions = []

for i  in range (1,5000):
    branch = random.choice([1,2])
    dr = random.choice(accs)
    cr = random.choice(accs)
    amount = random.randint(500, 10000)
    year = random.randint(2018, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = "%d-%d-%d"%(year,month,day)
    transaction={'date':date , 'id':i,'branch':branch,'debit':dr,'credit':cr,"amount":amount}
    # pprint (transaction)
    transactions.append(transaction)

csv_columns=[]
for k, v in transactions[0].items():
    csv_columns.append(k)

def post_csv_dict(data,csv_columns,filename):


    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except IOError:
        print("I/O error")

filename="/Users/aaronlee/Documents/python/fifthtutorial/post_exercises_3.csv"

post_csv_dict(transactions,csv_columns,filename)
