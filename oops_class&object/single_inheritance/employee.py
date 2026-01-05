
class Employee:

    def __init__(self,id,department,salary,):

        self.id =id

        self.department=department

        self.salary=salary

    def display(self):

        print(f"employee id ={self.id} department={self.department} salary={self.salary}")


class Developer(Employee):

    programming_language:str

    framework:str

    def __init__(self, id, department, salary,programming,framework):
        super().__init__(id, department, salary)   
        
        self.programming_language=programming

        self.framework=framework

    def display(self):
        super().display()

        print(f"language={self.programming_language} framework={self.framework}")

department_instance=Developer(1001,"hr",150000,"python","django")

department_instance.display()