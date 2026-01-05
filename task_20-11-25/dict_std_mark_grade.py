
std_name_mark ={"Aju": 92, "Binu": 76, "Chandru": 64}

std_name_grade ={k: ("A" if v >= 90 else "B" if v >= 75 else "C") for k,v in std_name_mark.items()}

print(std_name_grade)