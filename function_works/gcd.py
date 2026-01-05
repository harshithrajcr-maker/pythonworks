
def gcd(num1,num2):
    
    smallest_number=min(num1,num2)

    result=1

    for i in range(1,smallest_number+1):

        if num1%i==0 and num2%i==0:

            result=i

    return result

print(gcd(12,24))