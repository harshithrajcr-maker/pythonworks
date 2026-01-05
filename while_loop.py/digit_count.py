num = int(input("enter a number :"))#123

count=0

while(num!=0):#123!=0

    digit = num%10 #123%10=3

    count = count+1

    num = num//10 #123//10=12

print("digit count =",count)
     
