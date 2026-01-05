day = int(input("enter a number 1-7= "))

if day in range(1,6):
    print("weekday")

elif day in range(6,8):
    print("weekend")

else:
    print("invalid")