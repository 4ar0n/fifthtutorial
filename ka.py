
# 1.import csv FX_XAUUSD_intraday_60.csv
# 2.write a program trade according to the x% of y-days moving averages :buy or square
# 3.find an optimum value of x and y to maximize the profit
# 4.output the csv with the ma and decision made.
# 5.use matlab to plot the candlestick graph for the data


#Question 1
import csv
import requests
from pprint import pprint

CSV_URL = 'https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/FX_XAUUSD_intraday_60.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
  

#Question 2
def mvg_avg(list, record_no, no_of_days):
    sub_total=0
    for i in range(record_no, record_no + no_of_days):
        sub_total = sub_total + float(list[i][4])
    mvg_avg = sub_total/int(no_of_days)
    return float(mvg_avg)

def mvg_avg_buy_sell_strategy(list, x, no_of_days, capital, bite_size):

    cash_balance = capital
    no_of_shares = 0

    for i in range(1+no_of_days,len(list)):

        if float(list[i][4]) > mvg_avg(list,i - no_of_days,no_of_days)*(1+x) and cash_balance > float(list[i][4])*bite_size:
            cash_balance = cash_balance - float(list[i][4])*bite_size
            no_of_shares = no_of_shares + bite_size

        if float(list[i][4]) < mvg_avg(list,i - no_of_days,no_of_days)*(1-x) and no_of_shares > bite_size:
            cash_balance = cash_balance + float(list[i][4])*bite_size
            no_of_shares = no_of_shares - bite_size

    profit = int(cash_balance) + int(no_of_shares*float(list[len(list)-1][4])) - capital
    return profit

    # print("Cash Balance : " + str(int(cash_balance)))
    # print("No of Shares : " + str(no_of_shares))
    # # print(my_list[len(my_list)-1][4])
    # print("MV of Shares : " + str(int(no_of_shares*float(list[len(list)-1][4]))))
    # print("Profit : " + str(profit))


#Question 3

dict_profit={}
q = 0
best_days = 0
best_delta = 0
best_profit = 0

for d in range(2, 30):
    for r in range(1,2):
        
        profit = mvg_avg_buy_sell_strategy(my_list, r/100, d, 10000, 1)
        dict_profit_sub = {}
        dict_profit_sub["Days"] = d
        dict_profit_sub["Delta%"] = r
        dict_profit_sub["Profit"] = profit
        dict_profit["S" + str(q)] = dict_profit_sub
        q+=1
        if profit > best_profit:
            best_profit = profit
            best_days = d
            best_delta = r

pprint(dict_profit)

best_result ={}
best_result['Days'] = best_days
best_result['Delta'] = best_delta
best_result['Profit'] = best_profit

pprint(best_result)

# for key, value in dict_profit.items():
#   print(key, value)

# Question 4
with open('/Users/user/pycourse/Homework/csvfile.csv','w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows(dict_profit.items())


# Question 5

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/4ar0n/fifthtutorial/master/FX_XAUUSD_intraday_60.csv')

fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])