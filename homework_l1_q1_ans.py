price_A=[99,104,88,114,112,90,113,84,103,107,]
price_B=[108,89,117,111,119,111,85,82,81,111,]
price_C=[104,95,88,91,116,106,90,80,96,110,]
price_D=[91,119,116,111,101,87,112,107,81,113,]
price_E=[106,104,85,94,91,100,83,111,114,102,]


vol_A=[7000,8600,8800,8400,6600,9600,6400,6400,9000,10000,]
vol_B=[9800,9200,9600,6200,8000,6800,9200,9600,7200,8000,]
vol_C=[10000,7200,8400,7400,7400,8800,10000,9200,8600,6200,]
vol_D=[10000,9200,6600,7200,8400,8600,6200,9000,9800,9400,]
vol_E=[6000,7000,9600,8800,10000,8800,9200,7000,7000,9800,]

def average_list(list):
    total = 0
    for num in list:
        total += num
    average = total / len(list) # len() is a function to return the total number of element in a list.
    return average

# print (average_list(price_A))
# print (average_list(price_B))
# print (average_list(price_C))
# print (average_list(price_D))
# print (average_list(price_E))

from statistics import mean, stdev
# print (mean(price_A))

# def moving_average(list,day):
#     if day >=2:
#         return (mean(list[day-:day])/day)

def moving_average_3d(list,day):
    if day < 2:                     #since the its a 3-day average, any day <2 will give you a runtime error.
        average_3d = None           # and I would like to give a None result just to make it a full list.
    if day >= 2:
        average_3d = round((list[day]+list[day-1]+list[day-2])/3,1) #the logic is pretty intuitive to explain.
    # print (average_3d) to debug
    return average_3d

# moving_average_3d(vol_A,1)

# 1.3. purchase when spot volume and price is X% higher than the 3-day  MA and sell when its Y% lower than the 3 day MA

def trade(price_list,vol_list):

    for i in range (0,len(price_list)): #looping over the 0 to length of the list
        if i>=2: #intuitively, u conly trade at t >= 2
            # the below logic is pretty intuitive. (but i found that the strategy with two conditions are too restrictive, so just for learning purpose)
            if price_list[i]>moving_average_3d(price_list,i)*1.05 and vol_list[i]>moving_average_3d(price_list,i)*1.05:
                print("buy on day "+str(i))
            if price_list[i]<moving_average_3d(price_list,i)*1.05 and vol_list[i]<moving_average_3d(price_list,i)*1.02:
                print("sell on day "+str(i))


#1.4. You have $1,000,000 in your investment account. Write a program using the strategy 3. (but only for price) above in calculate the profit for the trade strategy for each of the stock. quantity for each purchase is 1000 shares and you cannot short sell.

#Lets change from 20% to 5% to make more trade to test our strategy

def trade_2(price_list,vol_list):
    balance = 1000000
    stocks_on_hand=0
    cost_of_stocks_on_hand=0
    for i in range (0,len(price_list)):
        if i>=2:
            if price_list[i]>moving_average_3d(price_list,i)*1.05:
                print("-Purchased on day %s at price = %s" %( str(i),str(price_list[i]) ) )  # I use % to insert variable into string so that the codes are clearer.
                stocks_on_hand+=1000
                cost_of_stocks_on_hand+=1000*price_list[i]
            if price_list[i]<moving_average_3d(price_list,i)*1.05:
                if stocks_on_hand >=1000:
                    stocks_on_hand-=1000
                    print("-Sold on day %s at price = %s \n" %( str(i),str(price_list[i]) ) )   #\n is an escape character for newline
                    profit =cost_of_stocks_on_hand-1000*price_list[i]
                    print ("The profit for the trade is %s"%str(profit))
                    balance+=profit
                    print ("The Balance of your account is %s \n"%str(balance))




print ("\nStock A")
trade_2(price_A,vol_A)
print ("\nStock B")
trade_2(price_B,vol_B)
print ("\nStock ")
trade_2(price_C,vol_C)
print ("\nStock D")
trade_2(price_D,vol_D)
print ("\nStock E")
trade_2(price_E,vol_E)



print (max(price_A))
print (min(price_A))
print (stdev(price_A))















