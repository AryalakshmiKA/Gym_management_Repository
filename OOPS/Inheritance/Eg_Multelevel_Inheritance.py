class College:
    def __init__(self):
        self.college_name = ""
        self.location = ""
        self.contact_number = ""
    def college_data(self):
        self.college_name = input("Enter College Name : ")
        self.location = input("Enter College Location :")
        self.contact_number = input("Enter the Contact Number :")
    def college_info(self):
        print("_____College Details_____")
        print("College Name     : ",self.college_name)
        print("Location         : ",self.location)
        print("Contact Number   : ",self.contact_number)
class Department(College):
    def __init__(self):
        self.dept_id = ""
        self.dept_name = ""
        self.hod  = ""
    def dept_data(self):
        self.dept_id = input("Enter Department ID : ")
        self.dept_name = input("Enter Department Name : ")
        self.hod = input("Enter HOD Name  : ")
    def dept_info(self):
        print("____Department Details_____")
        print("Department ID   : ",self.dept_id)
        print("Department Name : ",self.dept_name)
        print("HOD Name        : ",self.hod)
class Student(Department):
    def __init__(self):
        self.stud_id = ""
        self.name = ""
        self.course = ""
        self.place = ""
        self.mobil = ""
    def student_data(self):
        self.stud_id = input("Enter Student ID  : ")
        self.name = input("Enter Student Name : ")
        self.course = input("Enter Course : ")
        self.place = input("Enter Place : ")
        self.mobil = input("Enter Mobil Number : ")
    def student_info(self):
        print("____Student Details____")
        print("Student ID      :  ",self.stud_id)
        print("Student Name    :  ",self.name)
        print("Course          :  ",self.course)
        print("place           :  ",self.place)
        print("Mobile Number   :  ",self.mobil)


obj1 = Student()
obj1.student_data()
obj1.dept_data()
obj1.college_data()
obj1.student_info()
obj1.dept_info()
obj1.college_info()