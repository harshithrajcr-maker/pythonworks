num1 = int(input("enter the number1: "))

num2 = int(input("enter the number2: "))

last_digt_num1 = num1%10
last_digt_num2 = num2%10

sum = last_digt_num1+last_digt_num2

print(sum>5)