
class Course :

    def __init__(self,course_name):

        self.course_name=course_name

    def display(self):

        print(f"course name :{self.course_name}")

class Module(Course):

    def __init__(self, course_name,m_name):
        super().__init__(course_name)

        self.m_name =m_name

    def display(self):
         super().display()

         print(f"module name :{self.m_name}")

class Lesson(Module):

    def __init__(self, course_name, m_name,lesson_name):
        super().__init__(course_name, m_name)

        self.lesson_name=lesson_name

    def display(self):
        super().display()

        print(f"lesson name :{self.lesson_name}")

lesson_instance =Lesson("python django","oop","constractor")

lesson_instance.display()