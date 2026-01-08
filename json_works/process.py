from json import load

file_path="json_works\\student.json"

fr =open(file_path,"r",encoding="utf-8")

data =load(fr)

for st in data:

    print(st.get("name"),"\t" ,st.get("gender"))


course_ds =[ds.get("name") for ds in data if ds.get("course")=="ds"]

print(course_ds)

