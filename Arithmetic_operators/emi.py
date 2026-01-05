p = int(input("enter principle loan amount "))

r = int(input("enter intrest rate "))

n = int(input("enter number of instalment "))



emi = p*r/(12*100)*(1+r)**n/(1+r)**n-1

print("emi calculation= ",round(emi,2))