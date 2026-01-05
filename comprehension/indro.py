

arr = [3,4,5,6,7,8]

squares = [num**2 for num in arr]

print(squares)

cubes = [num**3 for num in arr]

print(cubes)

even = [num for num in arr if num%2==0]

print(even)

odd =[num for num in arr if num%2!=0]

print(odd)

num_gt_five =[num for num in arr if num>5]

print(num_gt_five)