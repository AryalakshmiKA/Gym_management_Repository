class Student:
    def __init__(self,name,course):
        self.student_name = name
        self.course = course
    def display(self):
        print("_____Student Details______")
        print("Name      :",self.student_name)
        print("Course    :",self.course)


object1 = Student("Kannan","FullStack")
object1.display()


object2 = Student("Naomika","Java")
object2.display()
