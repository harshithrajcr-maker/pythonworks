import csv

class AiDataset:

    data:list

    def __init__(self):

        file_path ="oops_class&object\\AI_Impact_on_Jobs_2030.csv"

        fr =open(file_path,"r",encoding="utf-8")

        reader =csv.DictReader(fr)

        self.data = [row for row in reader]

    def total_records(self):

        print(len(self.data))

    def display_first_records(self):

        print(self.data[0])

ai_instance =AiDataset()

ai_instance.total_records()

ai_instance.display_first_records()
