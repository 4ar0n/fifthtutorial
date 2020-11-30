
import csv 
from pprint import pprint
from datetime import datetime 
from collections import OrderedDict 

def get_csv_dict(file):
    data  =  []

    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            data.append(dict(row))
    # pprint (data)
    return data
    # return data

def post_csv_dict(data,csv_columns,filename):

    try:
        with open(output_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except IOError:
        print("I/O error")

def make_sma_dict(data,field_name,day):
    #trimmed_day_data is declared for to hold only the last data of the day
    trimmed_day_data=OrderedDict() 
    #sma_dict is the ultimate product of this function which provides a lookup table for "date" to "sma"
    sma_dict={}
    for entry in data:
        if entry['datetime'][11:] in ["11:00:00","20:00:00","21:00:00","22:00:00","23:00:00"]:
            trimmed_day_data[entry['datetime'][:10]]=float(entry[field_name])
        
        
        #create an empty dictionary with only date keys e.g. {"2017-01-09":0,"2017-01-10":0,.... }
        sma_dict[entry['datetime'][:10]] = "None"



    #below is the loop to insert the sma value into the dictionary.
    for date , sma in sma_dict.items():
        #1 . mark down the position of the array found for later use
        pos = None

        #2. for every date in the sma_dict , loop the trimmed data to find the index of the trimmed data where the date is found.
        for i in range (0,len(trimmed_day_data)):
            # its a little bit complicated because, unlike list its its not that straight forward to get the KEY of the dictionary, 
            # list(trimmed_day_data.items()) is the ith element , and then we need to turn it to the list, so that the key becomes the [0] of the list
            if date == list(trimmed_day_data.items())[i][0]: 
                pos = i 
                #once found, break the loop
                break
        

        # to make sure pos is found
        if pos is not None:

            first_day_str = (list(trimmed_day_data.items())[0][0])

            first_day = datetime.strptime(first_day_str, '%Y-%m-%d')
            today = datetime.strptime(date, '%Y-%m-%d')


            #list(trimmed_day_data).index(date) returns the index of the date in the trimmed_day_data
            # make sure there are day-number of data because calculating day-sma

            if list(trimmed_day_data).index(date) >= day :
                total = 0
                for j in range(pos-day,pos):
                # when pos is 7, j is 0 
                # then j is 1
                # then j is 2... until j is 6, when 7 data is added to the total and the sma is calculated.
                    
                    total += list(trimmed_day_data.items())[j][1]

                sma_dict[date] = round(total / day,2)


    return sma_dict




def insert_sma(data,day,field_name):
    for i in range (0,len(data)):
        data[i][field_name+"_sma"] = sma_dict.get(data[i]['datetime'][:10],None)
    return data

def trade(data,percentage,day,field_name):
    data = insert_sma( data , day , field_name )
    asset = profit = lot = 0
    for i  in range( 0,len(data) ):
        if data[i][field_name+"_sma"] != "None":

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
            else: 
                data[i]["decision"] = "Hold"



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
day = 3
sma_dict = make_sma_dict(au_raw_data,"close",day)
au_trade_data = trade(au_raw_data,0.01,day,"close")



# max_profit = best_rate = best_day = 0 

# start = 1
# end = 30
# for i in range (start,end):
#     rate =  i/1000
#     for day in range(3,21):
#         # print (rate,day)
#         au_trade_data = trade(au_raw_data,rate,day,"close")
#         if au_trade_data["profit"] > max_profit:
#             max_profit = au_trade_data["profit"] 
#             best_day = day
#             best_rate = rate

# print (max_profit , best_rate ,  best_day)
csv_columns=[]
# pprint (au_trade_data)
for k, v in au_trade_data['csv'][-1].items():
    csv_columns.append(k)
# pprint (csv_columns)

output_file = au_raw_file[:-4]+"_results.csv"
post_csv_dict(au_trade_data['csv'],csv_columns,output_file)
