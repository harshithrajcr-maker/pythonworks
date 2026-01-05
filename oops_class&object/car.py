
class Car:

    name:str
    brand:str
    price:int
    color:str

    def set_car(self,name,brand,price,color):

        self.name=name
        self.brand=brand
        self.price=price
        self.color=color

    def display(self):

        print("car name:",self.name)
        print("car brand:",self.brand)
        print("price:",self.price)
        print("color:",self.color)
        print("================")


car_instance1=Car()

car_instance1.set_car("swift","maruthi",800000,"gray")

car_instance2 =Car()

car_instance2.set_car("nano","tata",400000,"yellow")

car_instance1.display()

car_instance2.display()



