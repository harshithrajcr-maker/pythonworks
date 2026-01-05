file_path ="file_operations\Titanic\dataset.csv"

fr = open(file_path,"r")

row = fr.readline()

print(row)

# for line in fr:

#     lst=line.rstrip("\n").split(",")

#     id=lst[0]
#     survived=lst[1]
#     pclass=lst[2]
#     name=lst[3].lstrip('"')
#     gender=lst[5]
#     age=lst[6]
#     sib_sp=lst[7]
#     parch=lst[8]
#     fare=lst[10]
#     cabin=lst[11]

#     print(name,age,)