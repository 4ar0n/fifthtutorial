# Aaron is a tuition business owner with two centres at Prince Edward and Causeway bay respectively.
# His accounting system database is a typical relational database that you the entry has to be looked up to other table to become meaningful.
# The data for 2018 and 2019 are stored in post_exercises_3_db.csv
# Requirement:
# 3.1 download / and output the post_exercises_3_db.csv AS dictionary and transalate them into a meaningful data eg:
# {'amount': 8235, 'branch': 1,'credit': 9, 'date': '2019-11-4','debit': 42,'id': 4946}  ==>
# {'amount': 8235, 'branch': "Prince Edward",'credit': Cash, 'date': '2019-11-4','debit': Stationery,'id': 4946} 
# and then output to post_exercises_3_db2.csv
# 3.2
# Produce an Income statement for the year of 2019
# Where Income statement: REVENUES - EXPENSES = NET PROFIT
# LIST ALL ITEMS with items and amount (do not list 0 items)
# Produce a BALANCE SHEET  for the year of 2019
# Where ASSETS (of all time)= LIABILITIES (of all time) + CAPITAL (of all time) + NET PROFIT (of 2019)
# LIST ALL ITEMS with items and amount (do not list 0 items)
# 3.3
# Produce a branch comparative income statement and balance sheet for comparasion between Causeway Bay and Prince Edward for 2018.
# with the following format:
# ITEMS Pince Edward , Causeway Bay
# 3.4
# Procuce a year compartive balance sheet for comparasion between 2018 and 2019,% change is to be reported.
# with the following format: ITEMS 2018, 2019 ,% change




import csv
import requests
from pprint import pprint

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
def convert_branch(data, dict_branch_db):
    for k,v in dict_branch_db.items():
    #print(v["branch"])
        for i in data:
            #for x,y in i.items():
            #print(x)
            if i["branch"] == v["id"]:
                i["branch"]= v["branch"]

   # pprint(data[:3])
    return data


#def convert debit_account(data, dict_ac_type_db)


def convert_id_account( data, dict_ac_db):
    #pprint(data[:3])
    #pprint(dict_ac_db)

    for k,v in dict_ac_db.items():
        for entry in data:
            #for x,y in entry.items():


                if v["id"]== entry["credit"]:
                    entry["credit"]=v["account"]
                if v["id"] == entry["debit"]:
                    entry["debit"]=v["account"]
    return data
   # pprint(data[:10])



def output_csv(data, filename):
    csv_columns=["amount", "branch", "date", "debit", "id","credit"]
    #try:
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        #writer.writeheader()
        for row in data:
            writer.writerow(row)
    #except IOError:
     #   print("I/O error")


def get_csv_dict(url):
    data  =  []
    dict={}
    #print(url)
    with requests.Session() as csv_file:
        download=csv_file.get(url)
        decoded_content= download.content.decode("utf-8")
        #print(decoded_content)
        csv_reader = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    
    mylist= csv_reader
    #print(mylist)

    
    

    for row in csv_reader:
        data.append(row)

    for row in data:
        for k,v in row.items():
            try:
                row[k]=int(v)
            except:
                pass
    #pprint(data[:4])           

        #dict={"row"}
    #   print(row)
    # return data[0:5]
    
    #print(mylist)

    return data   



file="https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/post_exercises_3_db.csv"
 #get_csv_dict(file)

#db=requests.get(file)

data= get_csv_dict(file)

#pprint (data[:10])


def turn_list_into_dict(key,table):
    dict={}

    for row in table:
        dict[str(row[key])]= row # 1 : {1: xxxxx} 
     

    return dict


dict_ac_type_db=turn_list_into_dict("id",ac_type_db)
dict_branch_db=turn_list_into_dict("id", branch_db)
dict_ac_db=turn_list_into_dict("id", ac_db)
data= convert_branch(data, dict_branch_db)
data= convert_id_account(data, dict_ac_db)

filename="post_exercises_3_db2.csv"
output_csv(data, filename)



def income_statment(data, year, dict_ac_db, dict_ac_type_db):
    income_data=[]
    
    #pprint(data[:50])
    dict={}
    #pprint(data[:4])
    for entry in data:
        print(entry["date"][0:4])
        if(entry["date"][0:4]=="2019"):
            

            for k,v in dict_ac_db.items():

            
                if(entry["debit"]== v["account"]  ): 
             #   print(v["category"])
                    if (v["category"]==5):
                        dict= {"date": entry["date"],"ID":entry["id"],"DEBIT": entry["debit"],"credit": entry["credit"],"category": v["category"], "amount":entry["amount"] }
                        income_data.append(dict)
             
                if(entry["credit"]== v["account"]):
                    if (v["category"]==4):
                        dict= {"date": entry["date"],"ID":entry["id"],"DEBIT": entry["debit"],"credit": entry["credit"],"category": v["category"], "amount":entry["amount"] }
                        income_data.append(dict)

          
    #pprint(data[:10])
    for entry in income_data:
        pprint(entry)
    
    #for entry in income_data:
     #   if entry["category"]==4:
           # pprint(entry)



#income_data=[]
year="2019"
income_data=[{"account": 1, "amount":1 , "ac_category":1 } ]


#print(income_data)
income_data=income_statment(data, year, dict_ac_db, dict_ac_type_db)

#pprint(data[:10])
#for row in data[]:
 #   print(row)


#print(data[:3])


#print(dict_ac_type_db)


#1. checking the dictionary of data and put in branch key to change the value  to prince Edward

#[{'date': '2018-1-1', 'id': 1, 'branch': 1, 'debit': 1, 'credit': 2, 'amount': 500000}, {'date': '2018-1-1', 'id': 2, 'branch': 2, 'debit': 1, 'credit': 2, 'amount': 500000}]

#print(dict_branch_db)

# for entry in data[:3]:
#   for k, v in entry.items():
        
#       if k ==dict_branch_db[]
    

                #print(y)
                #print("kdsajklfjak")




#pprint(data[:5])
    #print( v["id"])







