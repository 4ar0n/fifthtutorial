import csv
from pprint import pprint

def import_csv(filepath):

    csv_data =[]

    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for row in csv_reader:
            csv_data.append(dict(row))
    return csv_data


def post_csv_dict(data,csv_columns,filename):

    try:
        with open(output_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except IOError:
        print("I/O error")
        
def cal_sma_from_csv(csv_data, field_name, record_no, no_of_days, hours_list):
    total = 0
    c = 0
    row_no = record_no
    while c < no_of_days and row_no > 0:
        if int(csv_data[row_no]['datetime'][11:13]) in hours_list or (hours_list ==[0]):
            total+=float(csv_data[row_no][field_name])
            c+=1
            row_no-=1
        else:
            row_no-=1

    if c < no_of_days:
        sma = 0
    else:
        sma = total/no_of_days

    return round(sma,2)

def add_sma_data_to_main(csv_data, field_name, no_of_days, hours_list):

    for i in range(0,len(csv_data)):
        csv_data[i][field_name + "_sma"] = cal_sma_from_csv(csv_data, field_name, i, no_of_days, hours_list)
    return csv_data

def trade_algro(csv_data, delta_percent, no_of_days, field_name, hours_list, capital,lot):

    trade_data = add_sma_data_to_main(csv_data, field_name, no_of_days,hours_list)
    cash_on_hand = capital
    asset = profit = shareholding = 0
    for i in range(0, len(trade_data)):
        if trade_data[i][field_name + "_sma"] == 0:
            trade_data[i]["decision"] = "hold"
            asset = float(trade_data[i][field_name])*shareholding
            profit = asset + cash_on_hand - capital             
        elif float(trade_data[i][field_name]) > trade_data[i][field_name + "_sma"]*(1+delta_percent):

            if cash_on_hand > float(trade_data[i][field_name])*lot:
                trade_data[i]["decision"] = "buy"
                cash_on_hand-= float(trade_data[i][field_name])*lot
                shareholding+=lot
                asset = float(trade_data[i][field_name])*shareholding
                profit = asset + cash_on_hand - capital 
            else:
                trade_data[i]["decision"] = "Not enough cash to buy"
                asset = float(trade_data[i][field_name])*shareholding
                profit = asset + cash_on_hand - capital

        elif float(trade_data[i][field_name]) < trade_data[i][field_name + "_sma"]*(1-delta_percent):
            
            if shareholding > lot:
                trade_data[i]["decision"] = "sell"
                cash_on_hand+= float(trade_data[i][field_name])*lot
                shareholding-=lot
                asset = float(trade_data[i][field_name])*shareholding
                profit = asset + cash_on_hand - capital 
            else:
                trade_data[i]["decision"] = "No holding to sell"
                asset = float(trade_data[i][field_name])*shareholding
                profit = asset + cash_on_hand - capital                             
        else:
            trade_data[i]["decision"] = "hold"
            asset = float(trade_data[i][field_name])*shareholding
            profit = asset + cash_on_hand - capital 

        trade_data[i]["Asset Value"] = round(asset,2)
        trade_data[i]["Cash On Hand"] = round(cash_on_hand,2)
        trade_data[i]["Shareholding"] = round(shareholding,2)
        trade_data[i]["Profit"] = round(profit,2)

    return trade_data

csv_raw_file = "/Users/aaronlee/pycourse/lesson2/datasets/FX_XAUUSD_intraday_60.csv"
csv_data = import_csv(csv_raw_file)
# print(csv_data[40]["datetime"])
# print(cal_sma_from_csv(csv_data, "close", 40, 3, [23]))
trade_data = trade_algro(csv_data, 0.01, 3, "close", [23], 100000,10)
# pprint(trade_data)

# dict_profit={}
# q = 0
# best_days = 0
# best_delta = 0
# best_profit = 0

# for d in range(3, 20):
#     for r in range(1,3):
#         trade_data = trade_algro(csv_data, r/100, d, "close", [23], 100000,10)
#         profit = trade_data[len(trade_data)-1]["Profit"]
#         dict_profit_sub = {}
#         dict_profit_sub["Days"] = d
#         dict_profit_sub["Delta%"] = r
#         dict_profit_sub["Profit"] = profit
#         dict_profit["S" + str(q)] = dict_profit_sub
#         q+=1
#         if profit > best_profit:
#             best_profit = profit
#             best_days = d
#             best_delta = r

# pprint(dict_profit)

# best_result ={}
# best_result['Days'] = best_days
# best_result['Delta'] = best_delta
# best_result['Profit'] = best_profit

# pprint(best_result)


