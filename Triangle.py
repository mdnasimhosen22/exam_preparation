# function use kore triangle er area ber korbo
import math
def triangle ():
    first_bahu = int(input("Enter your first number = "))
    second_bahu = int(input("Enter your second number = "))
    tried_bahu = int(input("Enter your tried number = "))

    if (( first_bahu + second_bahu ) > tried_bahu and
            (second_bahu + tried_bahu) > first_bahu and
            (tried_bahu + first_bahu) > second_bahu):

        s = (first_bahu + second_bahu + tried_bahu) / 2
        area = math.sqrt(s*(s-first_bahu)*(s-second_bahu)* (tried_bahu))
        print("Area of Triangle =", area)
    else:
        print("Sorry math Error")


triangle()


# use class

class triangle:
    def __init__(self):
        first_bahu = int(input("Enter your first number = "))
        second_bahu = int(input("Enter your second number = "))
        tried_bahu = int(input("Enter your tried number = "))

        if ((first_bahu + second_bahu) > tried_bahu and
                (second_bahu + tried_bahu) > first_bahu and
                (tried_bahu + first_bahu) > second_bahu):

            s = (first_bahu + second_bahu + tried_bahu) / 2
            area = math.sqrt(s * (s - first_bahu) * (s - second_bahu) * (tried_bahu))
            print("Area of Triangle =", area)
        else:
            print("Sorry math Error")


triangle()