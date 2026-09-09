import math


class Circle:
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return math.pi * (self.r ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.r

radius = int(input("Enter the Radius of Circle : "))
obj1 = Circle(radius)
area = obj1.calculate_area()
perimeter = obj1.calculate_perimeter()

print("Area of the Circle : ",int(area))
print("Perimeter of the Circle : ",int(perimeter))