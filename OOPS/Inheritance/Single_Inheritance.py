class Animal:
    def sound(self):
        print("Animal Make Sounds...")

class Dog(Animal):
    def bark(self):
        print("Dog Barks.....")

obj1 = Dog()
obj1.sound()
obj1.bark()