from decimal import *
getcontext().prec = 16
buy=Decimal(input("Enter buy price:"))
#sell=Decimal(input("Enter sell price:"))
def charges_calc(buy,sell):
	turnover=(buy+sell)
	brokerage=turnover*(Decimal(0.01) / Decimal(100))
	if(brokerage>=40):
		brokerage=Decimal(40)
	stt=sell*(Decimal(0.025) / Decimal(100))
	exch=(Decimal(0.00325) / Decimal(100))*turnover
	gst=(Decimal(18) / Decimal(100))*(brokerage+exch)
	duty=(Decimal(0.01) / Decimal(100))*turnover
	sebi=(Decimal(15) / Decimal(10000000))*turnover
	charges=brokerage+stt+exch+gst+duty+sebi
	profit=sell-buy-charges
	return profit
temp=buy
while(1):
	#sell=Decimal(input("Enter sell price:"))
	sell=temp+Decimal(0.05)
	print("Sell: " +str(sell))
	profit=charges_calc(buy,sell)
	print("Profit: " +str(profit))
	if(profit>=0):
		break
	temp=temp+Decimal(0.05)
#print(Decimal(15) / Decimal(10000000))
"""
while(1):
	sell=buy+Decimal(0.05)
	print("Sell: " +str(sell))
	profit=charges_calc(buy,sell)
	print("Profit: " +str(profit))
	if(profit>=0):
		break
	buy=buy+Decimal(0.05)
"""
