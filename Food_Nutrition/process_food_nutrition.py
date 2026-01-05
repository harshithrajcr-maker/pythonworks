
file_path = "Food_Nutrition\\Food_Nutrition_Dataset.csv"

fr =open(file_path,"r",encoding="utf-8")

import csv

reader =csv.DictReader(fr)

data =[row for row in reader]

# print(len(data))

# print all food names

food_names =[f.get("food_name") for f in data]

# print(food_names)

# print first 10 food names

first_10 =data [:11]

first_10_data =[f.get("food_name") for f in first_10]

# print(first_10_data)

all_catagory =[f.get("category") for f in data]

food_catogorys ={f:all_catagory.count(f) for f in all_catagory }

# print(food_catogorys)

#print apple items and total number of apple

apples_itms =[f for f in data if f.get("category")=="Apples"]

# print(apples_itms)

print(len(apples_itms))

#print highest calorie, and lowest calorie items

item_calorie = {dic.get("food_name"):float(dic.get("calories",0)) for dic in data}

#print(item_calorie)

lstmin=list()

lstmax=list()

max_calorie = max(item_calorie.values())

# print("max calorie",max_calorie)

min_calorie = min(item_calorie.values())

# print(" min calorie",min_calorie)

for k,v in item_calorie.items():

    if v==min_calorie:

        lstmin.append(k)

    elif v==max_calorie:

        lstmax.append(k)

# print(f"min calorie items= {lstmin,min_calorie}, max calorie items ={lstmax,max_calorie}")

#category wise count
data_category ={}

for f in data:

    if f.get("category") in data_category:
        
        data_category[f.get("category")]+=1
    else:
        data_category[f.get("category")]=1

print(data_category)

print(len(data_category))

#vitamin c list

vitamin_lst =[f.get("vitamin_c") for f in data]

print(vitamin_lst)





