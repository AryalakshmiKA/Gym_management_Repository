student = {"Name":"Arya",
           "Age": 31,
           "Gender":"Female",
           "course":"Python Fullstack",
           "skills":["Python", "JAVA", "Django","HTML"]
           }
for i in student:
    print(i)
print("___using keys()___")
for i in student.keys():
    print(i)
print("___Using Values()___")
for i in student.values():
    print(i)
print("___Using Items()___")
for i in student.items():
    print(i)
