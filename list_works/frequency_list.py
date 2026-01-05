
arr = [100,200,300,110,210,200,110,110,100]

freqent_num = []

for num  in arr:

     occ=arr.count(num)

     if occ>1 and num not in freqent_num:
     
       freqent_num.append(num)


print(freqent_num)