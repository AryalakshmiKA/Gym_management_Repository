class Employee:
    def __init__(self,id,name,place,company,salary,designation):
        self.emp_id = id
        self.emp_name = name
        self.emp_place = place
        self.company = company
        self.salary = salary
        self.designation = designation
    def display_employee_setails(self):
        print("____Employee Details_____")
        print("Employee ID     : ",self.emp_id)
        print("Employee Nameb  : ",self.emp_name)
        print("Place           : ",self.emp_place)
        print("Company         : ",self.company)
        print("Salary          : ",self.salary)
        print("Designation     : ",self.designation)


emp_obj1 = Employee(123,"Kannan","Kochi","DTDC",85000,"Assot.Manager")
emp_obj1.display_employee_setails()

emp_obj2 = Employee(365,"Arya","Palarivattom","SRBS",20000,"Asst.Professor")
emp_obj2.display_employee_setails()

emp_obj3 = Employee(785,"Anjana","Pala","Malabar trades",15000,"Accountant")
emp_obj3.display_employee_setails()