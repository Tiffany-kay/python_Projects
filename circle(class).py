#   code to calculate area and perimeter of a circle
from math import pi
#  class with methods to calculate area and perimeter
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    def calculate_area(self):
        return self.radius ** 2 * pi

    def calculate_perimeter(self):
        return 2 * pi * self.radius

rad = float(input("Enter the radius of the circle: "))
circle = Circle(rad)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.calculate_area()}")
print(f"Perimeter: {circle.calculate_perimeter()}")
 