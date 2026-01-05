
years = [2021,1999,1920,2024,1852,1991,2026,2000,2023,2016,2009]

leap_year = []

for y in years:

        if y%100==0 and y%400==0 or y%100!=0 and y%4!=0:
                
            leap_year.append(y)

print("leap years =",leap_year)
