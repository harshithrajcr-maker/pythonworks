
class Mobile :

    tittle :str

    price :int

    brand:str

    features :str

    def __init__(self,tittle,price,brand,features):

        self.tittle=tittle

        self.price=price

        self.brand=brand

        self.features=features     

    def display(self):

        print(f"tittle {self.tittle} price {self.price} brand {self.brand} features {self.features} ")


Mobile_instance1 =Mobile("s23",35000,"samsung","compact phone")

Mobile_instance2 =Mobile("iphone 13",55000,"Apple","camera")

Mobile_instance1.display()

Mobile_instance2.display()
        