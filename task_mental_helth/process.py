
file_path ="task_mental_helth\\mental_health_social_media_dataset.csv"

fr =open(file_path,"r",encoding="utf-8")

import csv

reader =csv.DictReader(fr)

data=[d for d in reader]

print(len(data))

all_platform =[p.get("platform") for p in data]

# print(all_platform)

# platform ={p:all_platform.count(p) for p in all_platform}

# print(platform)

platformwise={}

for p in data:

    platform1 = p.get("platform")

    if platform1 in platformwise:

        platformwise[platform1]+=1

    else:

        platformwise[platform1]=1

print("platform",platformwise)

print(max(platformwise.values()))

print(min(platformwise.values()))

# max and min of platform
max_platform =[k for k,v in platformwise.items() if v==max(platformwise.values())]
min_platform =[k for k,v in platformwise.items() if v==min(platformwise.values())]

print(max_platform)
print(min_platform)


