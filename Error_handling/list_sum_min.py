lst =["10","20","hello","300","hai","4 00"]

digit_lst =[]

for n in lst:

    try:
        
        num = int(n)
        
        digit_lst.append(num)

    except Exception as e:
        
        continue

print("numbers list\n",digit_lst)

max_element =max(digit_lst)

min_element =min(digit_lst)

srt_numbers =sorted(digit_lst)

total = sum(digit_lst)

print("max number\n",max_element)

print("min number\n",min_element)

print("sorted list\n",srt_numbers)

print("total\n",total)