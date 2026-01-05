age = int(input("Enter your age : "))

if age in range(0,6):
    print("free")

elif age in range(5,19):
    print("$10")

elif age in range(19,61):
    print("$60")

elif age in range(60,100):
    print("$15")

else:
    print("Invalid")

"""
5. Ticket Fare Based on Age
"""