def area_rectangle(length, width):
    area = int(length) * int(width)
    print("Rectangle area = ", area)


length = input("length? ")
width = input("width? ")
area_rectangle(length, width)


def area_circle(radius):
    area = 3.142 * radius
    print("Circle area= ", area)


area_circle(7)
