class Person:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.place = ""
        self.mobil = ""
        self.email = ""
    def person_data(self):
        self.name = input("Enter Name   : ")
        self.age = int(input("Enter Age : "))
        self.place = input("Enter Place : ")
        self.mobil = input("Enter Mobil Number : ")
        self.email = input("Enter Email ID : ")
    def person_info(self):
        print("_____Person Details_____")
        print("Name     :  ",self.name)
        print("Age      :  ",self.age)
        print("Place    :  ",self.place)
        print("Mobil    :  ",self.mobil)
        print("Email-ID :  ",self.email)
class Salary:
    def __init__(self):
        self.basic_salary = ""
        self.bonus = ""
        self.doj = ""
    def salary_data(self):
        self.basic_salary = int(input("Enter the Basic Salary : "))
        self.bonus = int(input("Enter the Bonus  : "))
        self.doj = input("Enter the Date of Join  :  ")
    def salary_info(self):
        print("_____Salary Details______")
        print("Basic Salary  : ",self.basic_salary)
        print("Bonus         : ",self.bonus)
        print("Date of Join  : ",self.doj)
class Employee(Person, Salary):
    def __init__(self):
        self.emp_id = ""
        self.designation = ""
    def employee_data(self):
        self.emp_id = input("Enter the Employee ID : ")
        self.designation = input("Enter Designation  : ")
    def employee_info(self):
        print("_____Employee Details______")
        print("Employee ID    :  ",self.emp_id)
        print("Designation    :  ",self.designation)

obj1 = Employee()
obj1.person_data()
obj1.employee_data()
obj1.salary_data()

obj1.person_info()
obj1.employee_info()
obj1.salary_info()