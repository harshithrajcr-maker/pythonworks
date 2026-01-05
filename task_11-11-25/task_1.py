
arr = [1,5,9,12,15,16,19,20]

even_numbers=[]

odd_numbers =[]

count_even_num=0

count_odd_num=0

for num in arr:

    if num%2==0:
        
        even_numbers.append(num)

        count_even_num+=1
        
    else:
        
       odd_numbers.append(num)
       
       count_odd_num+=1

print("even numbers =",even_numbers)
print("odd numbers =",odd_numbers)
print("count of even numbers =",count_even_num)
print("count of odd numbers =",count_odd_num)

