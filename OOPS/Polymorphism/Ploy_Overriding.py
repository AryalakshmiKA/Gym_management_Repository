class Shape:
    def draw(self):
        print("Drawing a shape..")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")


obj1 = Shape()
obj1.draw()


obj2 = Circle()
obj2.draw()

