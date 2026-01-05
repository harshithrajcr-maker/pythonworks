num =int(input("enter a number :"))#345

while(num!=0):#345!=0,34!=0,3!=0,0!=0

    last_digit=num%10 #345%10=5,34%10=4,3%10=3
   
    print(last_digit) #5,4,3
    
    num=num//10 #345//10=34(345/10=34.5),34//10=3,3//10=0