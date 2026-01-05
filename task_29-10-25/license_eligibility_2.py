age =int(input("enter the age ="))

if age<18:
    print("not eligibil due to age")

    
elif age>=18:
    print("you have eligible for licence")

    yes_no =(input("have you pass the test (yes/no) ="))

    if  yes_no=="yes":
        print("license approved")

    else:
        print("test not cleard")

"""
2. Driving License Eligibility

Task:
Ask for age.
If age ≥ 18:
Ask if test is passed (yes or no)
If yes → "License Approved"
Else → "Test not cleared"
Else → "Not eligible due to age"

"""