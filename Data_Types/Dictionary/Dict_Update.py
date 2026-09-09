student = {"Name":"Arya",
           "Age": 31,
           "Gender":"Female",
           "course":"Python Fullstack",
           "skills":["Python", "JAVA", "Django","HTML"]
           }
print(student)
student["Mobile"] = 9995156798
print(student)
print("Student Mobile Number:",student["Mobile"])

student["Name"] = "Aryalakshmi"
print(student)
print("Student Name :",student["Name"])

del student["Gender"]
print(student)


