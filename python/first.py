amount = float(input("Enter amount:"))
intrest = float(input("Enter intrest rate:"))
period = int(input("Enter Period:"))
value = 0
year = 1
while year <= period:
    value = amount + (intrest * amount)
    print("Year %d Rs. %.2f" %(year, value))
    amount = value 
    year = year + 1
    
