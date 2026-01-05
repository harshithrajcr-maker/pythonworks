"""
lambda function : anonymous function with single expression
"""

add_number = lambda n1,n2:n1+n2

print(add_number(100,200))

square =lambda n:n**2

print(square(4))

cube =lambda n:n**3

print(cube(2))

odd_even =lambda n:"odd" if n%2!=0 else "even"

print(odd_even(7))

is_negative =lambda n :"is negative" if n<0 else  "is positive"

print(is_negative(-5))

is_century_year = lambda n :"True" if n%100==0 else "False"

print(is_century_year(2020))