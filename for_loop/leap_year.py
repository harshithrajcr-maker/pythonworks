for num in range(1800,2026):

    if num%100==0 and num%400==0 or num%100!=0 and num%4==0:

        print(num)