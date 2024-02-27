#  code to calculate perimeter and area of rectangle using class function
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area=self.length*self.width
        return f"area of the rectangle {area}"

    def perimeter(self):
        perimeter= 2*(self.length+self.width)
        return f"perimeter of the rectangle {perimeter}"

rectangle=Rectangle(3,3)
print(rectangle.calculate_area())
print(rectangle.perimeter())
