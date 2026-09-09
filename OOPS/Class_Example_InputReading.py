class Student:
    def __init__(self):
        self.name = ""
        self.place = ""
        self.age = 0
    def student_data(self):
        self.name = input("Enter Student Name    : ")
        self.age = int(input("Enter Student Age  : "))
        self.place = input("Enter Student Place  : ")
    def student_Details(self):
        print("____Student Details____")
        print("Name      : ",self.name)
        print("Age       : ",self.age)
        print("Place     : ",self.place)

obj1 = Student()
obj1.student_data()
obj1.student_Details()