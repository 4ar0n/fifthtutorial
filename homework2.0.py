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

from pprint import pprint
from datetime import datetime

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
    print ("%s has bought a/an %s at a price of %s on %s."%(name,item,str(price),trans_time.strftime("%Y-%m-%d")))

# for transaction in data:
#     name_id = transaction[1]
#     name = person_mapping_dict[name_id]
    
#     good_id = transaction[2]
#     item = good_mapping_dict[good_id]

#     price= price_mapping_table[good_id]

#     trans_time=transaction[0]
#     print_trans(name, item, price,trans_time)



# def filter_trans(selected_name_id):
#     for transaction in data:
#         name_id = transaction[1]
#         name = person_mapping_dict[name_id]
    
#         good_id = transaction[2]
#         item = good_mapping_dict[good_id]

#         price= price_mapping_table[good_id]

#         trans_time=transaction[0]
#         if name_id == selected_name_id:
#             print_trans(name, item, price,trans_time)

# filter_trans(1)
full_list=[]
for i in range (0,5000):
    full_list.append(i)

# def filter_trans_2( selected_name_id = full_list , selected_good_id = full_list):

#     for transaction in data:
#         name_id = transaction[1]
#         name = person_mapping_dict[name_id]
    
#         good_id = transaction[2]
#         item = good_mapping_dict[good_id]

#         price= price_mapping_table[good_id]

#         trans_time=transaction[0]

#         if name_id in selected_name_id and good_id in selected_good_id:
#             print_trans(name, item, price,trans_time)

# filter_trans_2([1,2])

# def filter_trans_3( selected_name_id = full_list , selected_good_id = full_list , selected_month = full_list):

#     for transaction in data:
#         name_id = transaction[1]
#         name = person_mapping_dict[name_id]
    
#         good_id = transaction[2]
#         item = good_mapping_dict[good_id]

#         price= price_mapping_table[good_id]

#         trans_time=transaction[0]

#         if name_id in selected_name_id and good_id in selected_good_id and trans_time.month in selected_month :
#             print_trans(name, item, price,trans_time)

# filter_trans_3(selected_month=[5])

def filter_trans_3( selected_name_id = full_list , selected_good_id = full_list , selected_month = full_list):

    total_revenue =  0 
    for transaction in data:
        name_id = transaction[1]
        name = person_mapping_dict[name_id]
    
        good_id = transaction[2]
        item = good_mapping_dict[good_id]

        price= price_mapping_table[good_id]

        trans_time=transaction[0]

        if name_id in selected_name_id and good_id in selected_good_id and trans_time.month in selected_month:
            print_trans(name, item, price,trans_time)
            total_revenue += price

    print ("Total Revenue: %s"% str(total_revenue) ) 

filter_trans_3(selected_name_id = [1])


