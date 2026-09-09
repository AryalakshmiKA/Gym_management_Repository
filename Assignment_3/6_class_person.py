from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def calculate_age(self):
        today = date.today()
        self.age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            self.age -= 1
    def person_data(self):
        print("_____PERSON DATA_____")
        print("Name          : ",self.name)
        print("Country       : ",self.country)
        print("Date of Birth : ",self.dob)
        print("Age           : ",self.age)

p1 = Person("Manu","India",date(1994,10,18))
p1.calculate_age()
p1.person_data()