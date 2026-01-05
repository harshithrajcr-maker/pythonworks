
file_path ="instagram_analytics\\Instagram_Analytics.csv"

fr =open(file_path,"r",encoding="utf-8")

import csv

reader =csv.DictReader(fr)

data =[row for row in reader]

# print length of data

# print(len(data))

all_content_category = [co.get("content_category") for co in data]

# print(all_content_category)

# print all content_category

content_category ={co:all_content_category.count(co) for co in all_content_category}

# print(content_category) 

# print the count of content_category

content_category = {}

for co in data:

    category = co.get("content_category")

    if category in content_category:

        content_category[category] += 1
    else:
        content_category[category] = 1

print("content and counts =", content_category)

# print max and min

max_content =max(content_category.values())

min_content = min(content_category.values())

print(max_content)

print(min_content)

#print the highest content category

max_content_ca = [k for k,v in content_category.items() if v==max_content]

min_content_ca = [k for k,v in content_category.items() if v==min_content]

# print ("Highest content : ",max_content_ca)

# print ("Lowest content : ",min_content_ca)

#print of all mediatype
all_mediatype = {md.get("media_type") for md in data}
print(all_mediatype)




