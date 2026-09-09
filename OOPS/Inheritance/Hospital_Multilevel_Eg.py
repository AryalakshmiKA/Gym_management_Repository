class Hospital:
    def __init__(self):
        self.hospital_name = ""
        self.location = ""
        self.hospital_contact = ""
    def hospital_data(self):
        self.hospital_name = input("Enter Hospital Name : ")
        self.location = input("Enter Hospital Location : ")
        self.hospital_contact = input("Enter Hospital Contact No : ")
    def hospital_info(self):
        print("_____Hospital Details______")
        print("Hospital Name   : ",self.hospital_name)
        print("Location        : ",self.location)
        print("Contact Number  : ",self.hospital_contact)

class Department(Hospital):
    def __init__(self):
        self.dept_id = ""
        self.dept_name = ""
        self.hod = ""
    def dept_data(self):
        obj.hospital_data()
        self.dept_id = input("Enter Department ID : ")
        self.dept_name = input("Enter Department Name : ")
        self.hod = input("Enter HOD Name : ")
    def dept_info(self):
        obj.hospital_info()
        print("____Department Details___")
        print("Department ID        : ",self.dept_id)
        print("Department Name      : ",self.dept_name)
        print("Department HOD Name  : ",self.hod)

class Patient(Department):
    def __init__(self):
        self.p_id = ""
        self.name = ""
        self.age = ""
        self.place = ""
        self.illness = ""
        self.contact = ""
    def patient_data(self):
        obj.dept_data()
        self.p_id = input("Enter Patient ID : ")
        self.name = input("Enter Patient Name : ")
        self.age = input("Enter Age : ")
        self.place = input("Enter Place : ")
        self.illness = input("Enter Illness : ")
        self.contact = input("Enter Contact Number : ")
    def patient_info(self):
        obj.dept_info()
        print("_____Patient Details_____")
        print("Patient ID     : ",self.p_id)
        print("Patient Name   : ",self.name)
        print("Age            : ",self.age)
        print("Place          : ",self.place)
        print("Illness        : ",self.illness)
        print("Contact Number : ",self.contact)

obj = Patient()
obj.patient_data()
obj.patient_info()
