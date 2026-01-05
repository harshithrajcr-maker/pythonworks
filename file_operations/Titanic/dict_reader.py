
file_path ="file_operations\\Titanic\\dataset.csv"

fr =open(file_path,"r")

import csv

reader =csv.DictReader(fr)

data = [row for row in reader]

print(len(data))

passenger_count =len(data)

# print(passenger_count)

passenger_name =[r.get("Name") for r in data]

# print(passenger_name)

genders = [p.get("Sex") for p in data]

male_count =genders.count("male")

female_count = genders.count("female")

# print("male count =",male_count)

# print("female count =",female_count)

survived = [s.get("Survived") for s in data]

survived_count =survived.count("1")

unsurvived_count = survived.count("0")

# print("Survived count =",survived_count)
# print("Unsurvived count =",unsurvived_count)

# pclass = [p.get("Pclass") for p in data]

# class_count = {c:pclass.count(c) for c in pclass}

# print(class_count)

# all_age = [int(p.get("Age")) for p in data if p.get("Age").isdigit()]

# youngest_age =min(all_age)

# oldest_age =max(all_age)

# youngest_person = [ for p in data if p.get("Age").isdigit() and int(p.get("Age"))]



first_ten =data[:11]

first_ten_names =[p.get("Name") for p in first_ten]

# print(first_ten_names)

boarding_stations = [p.get("Embarked") for p in data if len(p.get("Embarked"))>0]

boarding_count ={p:boarding_stations.count(p) for p in boarding_stations}

# print(boarding_count)


below_age_10 = [p for p in data if p.get("Age").isdigit() and int(p.get("Age"))<10]

# print(len(below_age_10))

survived_childrens =[p for p in below_age_10 if p.get("Survived")=="1"]

# print(len(survived_childrens))

survived_rate=[p.get("Survived") for p in data if p.get("Survived")=="1"]

survived_len =len(survived_rate)

percentage =(survived_len/passenger_count)*100

# print(percentage)


male_passengers = [p for p in data if p.get("Sex")=="male"]

male_survived =[p for p in male_passengers if p.get("Survived")=="1"]

male_survived_rate =(len(male_survived)/len(male_passengers))*100

# print(male_survived_rate)


female_passengers = [p for p in data if p.get("Sex")=="female"]

female_survived =[p for p in female_passengers if p.get("Survived")=="1"]

female_survived_rate =(len(female_survived)/len(female_passengers))*100

# print(female_survived_rate) 

survived_p=[p for p in data if p.get("Survived")=="1"]

pclass = [p.get("Pclass") for p in survived_p]

class_survived_count = {c:pclass.count(c) for c in pclass}

# print(class_survived_count)

# for k,v in class_survived_count.items():




