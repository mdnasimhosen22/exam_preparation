# use function
import math

def circle():
    radius = int(input("Enter your radius value = "))
    area = math.pi * radius**2
    print(f"Area of Circle = {area: .2f}")  # .2f mane . er por 2 ta number thakbe


circle()

# use class


class circle:
    def __init__(self):
        radius = int(input("Enter your radius value = "))
        area = math.pi * radius ** 2
        print("Area of Circle = {:.2f}".format(area))


circle()
