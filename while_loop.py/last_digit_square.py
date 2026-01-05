num = int(input("enter number :"))

while(num!=0):

    last_digit=num%10

    last_digit=last_digit**2

    print(last_digit)

    num=num//10
