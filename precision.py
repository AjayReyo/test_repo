from decimal import *
getcontext().prec = 16
buy=Decimal(input("Enter buy price:"))
sell=Decimal(input("Enter sell price:"))
turnover=(buy+sell)
brokerage=turnover*(Decimal(0.01) / Decimal(100))
stt=sell*(Decimal(0.025) / Decimal(100))
exch=(Decimal(0.00325) / Decimal(100))*turnover
gst=(Decimal(18) / Decimal(100))*(brokerage+exch)
duty=(Decimal(0.01) / Decimal(100))*turnover
sebi=(Decimal(15) / Decimal(10000000))*turnover
charges=brokerage+stt+exch+gst+duty+sebi
print(charges)
#print(Decimal(15) / Decimal(10000000))