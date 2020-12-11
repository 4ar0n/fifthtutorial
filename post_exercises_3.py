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

accs = [8,12,13]
# for ac in ac_db:
# 	accs.append(ac['id'])
# pprint (accs)


transaction=[]
transaction.append({'date':"2018-1-1" , 'id':1,'branch':1,'debit':1,'credit':2,"amount":500000})
transaction.append({'date':"2018-1-1" , 'id':2,'branch':2,'debit':1,'credit':2,"amount":500000})
transaction.append({'date':"2018-1-5" , 'id':3,'branch':1,'debit':9,'credit':5,"amount":300000})
transaction.append({'date':"2018-8-25" , 'id':4,'branch':2,'debit':1,'credit':14,"amount":200000})    

for i  in range (5,5000):
    branch = random.choice([1,2])
    amount = random.randint(500, 10000)
    year = random.randint(2018, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = "%d-%d-%d"%(year,month,day)
    transactionsdb=[
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},    
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':1,'debit':9,'credit':4,"amount":920},    
    {'date':date , 'id':i,'branch':2,'debit':9,'credit':4,"amount":920},
    {'date':date , 'id':i,'branch':random.choice([1, 2]),'debit':12,'credit':4,"amount":random.randint(15, 200)},
    {'date':date , 'id':i,'branch':random.choice([1, 2]),'debit':5,'credit':1,"amount":random.randint(800, 5000)},
    {'date':date , 'id':i,'branch':random.choice([1, 2]),'debit':13,'credit':9,"amount":random.randint(20, 300)},
    {'date':date , 'id':i,'branch':random.choice([1, 2]),'debit':6,'credit':1,"amount":random.choice([8000, 9000])},
    {'date':date , 'id':i,'branch':random.choice([1, 2]),'debit':7,'credit':1,"amount":random.choice([1500,4300,8500])},

    ]
    transaction.append(transactionsdb[random.randint(0, len(transactionsdb)-1)])

# pprint (transaction)

pprint (transaction[0])
csv_columns=[]
for k, v in transaction[0].items():
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

filename="/Users/aaronlee/Documents/python/fifthtutorial/post_exercises_3_db.csv"

post_csv_dict(transaction,csv_columns,filename)