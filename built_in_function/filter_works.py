
lst =[2,3,4,5,6,7,8,9,10,11,13,14,12]

evens =list(filter(lambda n:n%2==0,lst))

print(evens)

odds =list(filter(lambda n:n%2!=0,lst))

print(odds)

num_gt_five =list(filter(lambda n:n>5,lst))

print(num_gt_five)