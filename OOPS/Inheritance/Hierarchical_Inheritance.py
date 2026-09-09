class Employee:
    def company(self):
        print("Compant Name : Liminar Technolab..")
class Manager(Employee):
    def manger(self):
        print("Manger Manage the Team...")
class Developer(Employee):
    def code(self):
        print("Developer Writes the Code...")



obj1 = Manager()
obj1.company()
obj1.manger()

obj2 = Developer()
obj2.company()
obj2.code()