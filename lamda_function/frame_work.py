

person_age ={
    "adwaid" :20,
    "harshith":21,
    "amala":23,
    "arun":22
}

srt_person_age = sorted(person_age,key=lambda k:person_age.get(k),reverse=True)

# print(srt_person_age)

employee =[
    ["sam",34000,4],
    ["ram",44000,3],
    ["jacobe",54000,5],
    ["tahrun",74000,6],
    ["jibin",24000,1],
]

srt_emp_exp =sorted(employee,key=lambda lst:lst[2])

print(srt_emp_exp)

srt_emp_sal =sorted(employee,key=lambda  sal:sal[1])

print(srt_emp_sal)