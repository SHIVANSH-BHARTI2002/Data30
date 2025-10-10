class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,x,y):
        return x*y
    
class Circle(Shape):
    def area(self,r):
        return 3.14*r**2

rect = Rectangle()
circle = Circle()
print("Area of rectangle = %.2f \n Area of Circle = %.2f"%(rect.area(2,3),circle.area(4)))
    