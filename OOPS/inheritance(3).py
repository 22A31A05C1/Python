class Shape:
    def area(self):
        print("Calculating area")
class Circle(Shape):
    def area(self):
        print("Area of Circle: n * r**")
class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle: length + breadth")
circle=Circle()
rectangle=Rectangle()
circle.area()
rectangle.area()