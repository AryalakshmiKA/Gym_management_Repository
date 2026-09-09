
class Company:
    def __init__(self):
        self.company_name = ""
        self.location = ""
    def company_data(self):
        self.company_name = input("Enter Company Name  : ")
        self.location = input("Enter Company Locatoion : ")
    def company_info(self):
        print("___Company Details___")
        print("Company Name           : ",self.company_name)
        print("Company Location       : ",self.location)
class Employee(Company):
    def __init__(self):
        self.emp_name = ""
        self.email = ""
        self.designation = ""
        self.place = ""
    def employee_data(self):
        self.emp_name = input("Enter Employee Name : ")
        self.email = input("Enter Employee Email ID :")
        self.designation = input("Enter Designation :")
        self.place = input("Enter the Place :")
    def employee_info(self):
        print("____Employee Details____")
        print("Employee Name   : ",self.emp_name)
        print("Employee E-MAil : ",self.email)
        print("Designation     : ",self.designation)
        print("Place           : ",self.place)


obj1  = Employee()
obj1.employee_data()
obj1.company_data()
obj1.employee_info()
obj1.company_info()