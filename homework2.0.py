# dict_1 = [
    

#     "id":1,
#     "name":"John",
#     "join_date":"2020-03-20",
#     "gender":"M",
#     "mobile":"96124242",
#     "email":"john_099@gmail.com",




# ]

person_mapping_dict = {1:Aaron",2:"Vincent",3:"Sir Ying",4:"Jason",5:"Billy"}
good_mapping_dict = {45,"banana",46,"apple",47,"melon",48,"orange"}
price_mapping_table = [[45,4],[46,6],[47,20],[48,3]]

from pprint import pprint
from random import *
# from datetime import date 
from datetime import datetime
# data= []
# for i in range (1,50):
#     data.append([ date(2020,randint(1, 12),randint(1, 28)) , randint(1, 5) , randint(45, 48)])
# pprint (data)

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


person_db = [
                ["Aaron",False,28,["Basketball","100m","Teaching Competition"]],
                ["Twiggy",True,29,["Mahjong","Nothing at all"]],
                ["Billy",False,31,["Scam","etoro"]],
                ["Jason",False,33,["Butterfly Stroke", "1+1-you"]],
            ]
            
def print_trans(name, item, price,trans_time):
    print ("%s has bought a/an %s at a price of %s on %s"%(name,item,str(price),trans_time.strftime("%Y-%m-%d")))

for datum in data:
    
    for kv in person_mapping_table:
        if datum[1] == kv[0]:
            name =kv[1]

    for kv in good_mapping_table:
        if datum[2] == kv[0]:
            good = kv[1]

    for kv in price_mapping_table:
        if datum[2] == kv[0]:
            price = kv[1]

    print_trans(name, good, price,datum[0])









