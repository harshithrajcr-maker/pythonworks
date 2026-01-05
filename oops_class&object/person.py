
class Person:

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    @property

    def get_age(self):

        print(self.age)

    @property

    def get_gender(self):

        print(self.gender)
    

person_instance=Person("harsh",21,"male")

person_instance.get_age

person_instance.get_gender

print(person_instance.name)
        