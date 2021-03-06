from pprint import pprint
from random import *
from datetime import datetime

person_mapping_dict = { 1:"Aaron",
                        2:"Vincent",
                        3:"Sir Ying",
                        4:"Jason",
                        5:"Billy"   }
                        
good_mapping_dict = {   45:"banana",
                        46:"apple",
                        47:"melon",
                        48:"orange" }

price_mapping_table = { 45:4,
                        46:6,
                        47:20,
                        48:3, }

data=[[datetime(2020, 1, 6), 3, 45],
 [datetime(2020, 1, 10), 1, 48],
 [datetime(2020, 1, 28), 3, 45],
 [datetime(2020, 2, 2), 4, 48],
 [datetime(2020, 2, 15), 3, 45],
 [datetime(2020, 2, 23), 4, 45],
 [datetime(2020, 3, 5), 4, 45],
 [datetime(2020, 3, 6), 2, 45],
 [datetime(2020, 3, 8), 2, 48],
 [datetime(2020, 3, 20), 1, 45],
 [datetime(2020, 4, 26), 4, 47],
 [datetime(2020, 4, 28), 3, 46],
 [datetime(2020, 5, 17), 1, 47],
 [datetime(2020, 5, 18), 1, 47],
 [datetime(2020, 5, 28), 3, 47],
 [datetime(2020, 6, 9), 2, 46],
 [datetime(2020, 6, 12), 2, 46],
 [datetime(2020, 6, 16), 2, 47],
 [datetime(2020, 6, 22), 5, 48],
 [datetime(2020, 6, 24), 5, 48],
 [datetime(2020, 7, 4), 4, 46],
 [datetime(2020, 7, 9), 4, 45],
 [datetime(2020, 7, 20), 5, 48],
 [datetime(2020, 7, 22), 4, 45],
 [datetime(2020, 7, 25), 2, 47],
 [datetime(2020, 7, 26), 5, 45],
 [datetime(2020, 7, 28), 3, 46],
 [datetime(2020, 7, 28), 4, 48],
 [datetime(2020, 8, 2), 5, 46],
 [datetime(2020, 8, 3), 4, 46],
 [datetime(2020, 8, 6), 1, 48],
 [datetime(2020, 8, 7), 3, 48],
 [datetime(2020, 8, 28), 1, 48],
 [datetime(2020, 9, 3), 4, 48],
 [datetime(2020, 9, 26), 1, 47],
 [datetime(2020, 9, 28), 3, 47],
 [datetime(2020, 10, 7), 3, 47],
 [datetime(2020, 10, 9), 1, 46],
 [datetime(2020, 10, 20), 3, 47],
 [datetime(2020, 10, 22), 1, 46],
 [datetime(2020, 10, 22), 2, 48],
 [datetime(2020, 10, 23), 3, 48],
 [datetime(2020, 10, 27), 3, 48],
 [datetime(2020, 11, 1), 2, 47],
 [datetime(2020, 11, 17), 4, 46],
 [datetime(2020, 11, 24), 2, 48],
 [datetime(2020, 12, 5), 1, 45],
 [datetime(2020, 12, 10), 4, 45],
 [datetime(2020, 12, 28), 5, 46]]


Question 1a
Write a script to show the transactions in the data above. e.g.: 'Aaron has bought a/an orange at a price of 3 on 2020-01-10.'
Give the total revenue at then as a summary: "Total Revenue: 40"




Question 1b
Write a FUNCTION to show filtered transactions by name_id in the above.

def transaction_filter(1):
    ...
    print and return transactions-of-name_id=1

Question 1c (*advanced)
Write a FUNCTION to show filtered transactions by name_id ,  good_id  and month, *PLUS your function need to capable of showing all transactions or filter just good_id or just name_id etc.



