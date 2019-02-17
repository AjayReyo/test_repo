buy=int(input("Enter buy price:"))
#sell=int(input("Enter sell price:"))
#quan=int(input("Enter quanity:"))
def calc_charges(buy,sell,quan):        
    turnover=(buy+sell)*quan
    brokerage=round(0.01/100*turnover, 2)
    stt=round(0.025/100*sell*quan,0)
    exch=round(0.00325/100*turnover,2)
    gst=round(18/100*(brokerage+exch),2)
    duty=round(0.01/100*turnover,2)
    sebi=round(15/10000000*turnover,2)
    charges=brokerage+stt+exch+gst+duty+sebi
    return charges
#charges(buy,sell,quan)
temp=buy
for i in range(-15,25):
    temp=buy+(buy/1000*i)
    print("Sell:" + str(temp), end=" ")
    tax=round(calc_charges(buy,temp,10),2)
    print("End:" +str(round(buy+temp-buy-tax,2)))
