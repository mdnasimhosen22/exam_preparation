# function use kore আয়তন বের করার programme
def area():
    length = int(input("Enter your length ="))
    width = int(input("Enter your width ="))


    area = length * width
    print("Area of Triangle =", area)

area()

# class use kore আয়তন বের করার programme

class area:
    def __init__(self):
        length = int(input("Enter your length ="))
        width = int(input("Enter your width ="))

        area = length * width
        print("Area of Triangle =", area)

area()
