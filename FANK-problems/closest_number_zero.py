
class closesetNumberToZero:

    def solution(self,arr):

        closeset_number =arr[0]

        for num in arr:

            if abs(num) < abs(closeset_number):

                closeset_number=num

        if closeset_number<0 and abs(closeset_number) in arr:

            return abs(closeset_number)
        
        else:

            return closeset_number
    

clst_instance =closesetNumberToZero()

print(clst_instance.solution([-1,-2,-3,2,3,4,1]))

# abs used to change nagative number to positive number