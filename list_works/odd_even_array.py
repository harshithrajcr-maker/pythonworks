
arr = [3,4,12,13,14,20,22]

even_array =[]

odd_array = []

for num in arr:

    if num%2==0:

        even_array.append(num)

    else:

        odd_array.append(num)

print("even array\n",even_array)

print("odd array\n",odd_array)