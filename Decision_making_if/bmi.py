height_in_cm =int(input("enter the height cm ="))

weight =int(input("enter the  in kg ="))

height_in_meter =height_in_cm/100

bmi =weight/(height_in_meter**2)

bmi =round(bmi,0)

print(bmi)

if bmi<20 :
    print("underweight")

elif bmi<25:
    print("normal")

elif bmi<30:
    print("overweight")

else:
    print("obse")
    