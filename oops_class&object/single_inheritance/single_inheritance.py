
class Person:

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display(self):

        print(f"name={self.name}age={self.age} gender={self.gender}")

class Student(Person):

    roll_no :str

    course :str

    def __init__(self, name, age, gender,roll,course):

        super().__init__(name, age, gender)

        self.roll_no =roll

        self.course =course

    def display(self):
        
         super().display()

         print(f"roll no ={self.roll_no} course ={self.course}")

student_instance =Student("harshith",21,"male",32,"django")

student_instance.display()



        