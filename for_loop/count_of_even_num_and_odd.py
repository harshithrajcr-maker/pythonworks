limit = int(input("Enter limit :"))

even_count = 0

odd_count = 0

for i in range(1,limit+1):

    if i%2==0:

        even_count=even_count+1

    else:
        odd_count=odd_count+1


print(even_count)

print(odd_count)