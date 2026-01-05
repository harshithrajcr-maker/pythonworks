
import csv

class AmazonSales:

    data:list

    def __init__(self):
        
        file_path="task_amazon_sales\\amazon_sales_2025_INR_cleaned.csv"

        fr =open(file_path,"r",encoding="utf-8")

        reader =csv.DictReader(fr)

        self.data =[row for row in reader ]

    def total_records(self):

        print(len(self.data))

    def display_first_record(self):

        print(self.data[0])

    def get_dimensions(self):

        dimension=[d.get("Dimension") for d in self.data]

        print(dimension)

    def category_performans(self):

        cat_per =[c for c in self.data if c.get("Report_Section")=="CATEGORY_PERFORMANCE"]
        
        print(cat_per)
    
amazon_instance =AmazonSales()

# amazon_instance.total_records()

# amazon_instance.display_first_record()

# amazon_instance.get_dimensions()

amazon_instance.category_performans()



