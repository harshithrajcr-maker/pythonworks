cibil =int(input("enter the cibil scor ="))

if cibil in range(300,550):
    print("poor")

elif cibil in range(550,650):
    print("average")

elif cibil in range(650,750):
    print("good")

elif cibil in range(750,901):
    print("excellent")

else:
    print("invalid")