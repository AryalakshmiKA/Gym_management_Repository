import random

from Data_Types.Dictionary.Dict_employee import employee

print(random.randint(1,50))
print(random.random())
student = ["Arya", "Anu","Zen"]
random.shuffle(student)
print(student)

employee = ["Manu","Jain","Kumar"]
print(random.choice(employee))
print(random.choices(employee))