
import csv 
from pprint import pprint


def get_csv_dict(file):
    data  =  []

    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            data.append(dict(row))
    # return data[0:5]
    return data

def post_csv_dict(data,csv_columns,filename):

    try:
        with open(output_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except IOError:
        print("I/O error")
# [ 0, 1, 2, 3, 4, 5, 6, 7, 8]
# [10,15,16,16,13,14,15,18,29]
#            X
# day =3
# starting = 3
# (data[day-3]+data[day-2]+data[day-1])/day


def get_sma_from_csv(data,field_name,date_th,day):
    total = 0
    for i in range(date_th-day,date_th):
        total += float(data[i][field_name])
    sma = total / day
    return round(sma,2)


def insert_sma(data,day,field_name):
    for i in range (day,len(data)):
        data[i][field_name+"_sma"]= get_sma_from_csv(data,field_name,i,day)
    return data

def trade(data,percentage,day,field_name):
    data = insert_sma( data , day , field_name )
    asset = profit = lot = 0
    for i  in range( day,len(data) ):
        if float(data[i][field_name]) > data[i][field_name+"_sma"]*(1+percentage):
            data[i]["decision"] = "Buy"
            lot +=1
            asset += float(data[i]['close'])
        elif float(data[i][field_name]) < data[i][field_name+"_sma"]*(1-percentage):
            if lot>0:

                data[i]["decision"] = "Square"

               
                cost = asset
                asset = 0

                revenue = float(data[i]['close'])*lot
                lot = 0 

                profit += (revenue - cost)


        else: 
            data[i]["decision"] = "Hold"



    # print ("Profit:  %s" % "${:,.2f}".format(profit))
    # print ("Assets:  %s" % "${:,.2f}".format(asset))
    # print ("Lot : %s"% str(lot))
    # pprint (data)
    output = {
        "csv" : data,
        "profit" : profit,
        "asset" : asset,
        "lot" : lot,
    }

    return output

au_raw_file = "/Users/aaronlee/pycourse/lesson2/datasets/FX_XAUUSD_intraday_60.csv"
au_raw_data = get_csv_dict(au_raw_file)
# pprint (au_raw_data)
# day = 7
# au_trade_data = trade(au_raw_data,0.02,day,"close")

max_profit = best_rate = best_day = 0 

start = 1
end = 30
for i in range (start,end):
    rate =  i/1000
    for day in range(3,21):
        # print (rate,day)
        au_trade_data = trade(au_raw_data,rate,day,"close")
        if au_trade_data["profit"] > max_profit:
            max_profit = au_trade_data["profit"] 
            best_day = day
            best_rate = rate

print (max_profit , best_rate ,  best_day)
csv_columns=[]
for k, v in au_trade_data[day].items():
    csv_columns.append(k)
output_file = au_raw_file[:-4]+"_results.csv"
post_csv_dict(au_trade_data[data],csv_columns,output_file)
