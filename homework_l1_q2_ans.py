from numpy_financial import pmt # I "pip3 install numpy_financial" to get pmt function and the rest is pretty intuitive

def mortgage_schedule(principal,interest_rate,months):
    monthly_interest_rate = pow(1+interest_rate,(1/12))-1
    monthlyPayment = -round(pmt(monthly_interest_rate, months, principal),1)
    for i in range(0,months):
        interest = round(monthly_interest_rate*principal,1)
        repayment = monthlyPayment - interest
        print (i,"\t", round(principal,1),"\t",monthlyPayment,"\t",interest,"\t",round(principal - repayment,1),"\t")
        principal = round(principal - repayment,1)

mortgage_schedule(4000000,0.0215,30*12)


