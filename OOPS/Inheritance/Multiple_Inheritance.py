from OOPS.Constructor_Example import Obj


class Father:
    def father_skills(self):
        print("Driving....")

class Mother:
    def mother_skills(self):
        print("Cooking.....")

class Child(Father, Mother):
    def child_skills(self):
        print("Studing....")

obj = Child()
obj.child_skills()
obj.mother_skills()
obj.father_skills()