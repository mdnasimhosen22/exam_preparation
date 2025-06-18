# class use kore Dighat shomikoron ber korar programme
class dighat:
    def __init__(self):
        a = int(input("enter the value a:"))
        b = int(input("enter the value b:"))
        c = int(input("enter the value c:"))
        import math
        d = (b**2) -(4*a*c)
        print(f"\n Discriminant (D) = {d}")   # (optional)
        if d < 0:
            print("No Answer it's a invalid number--")
        else:
            sol1 = (-b + math.sqrt(d) / 2 * a)
            sol2 = (-b - math.sqrt(d) / 2 * a)
            print(f"result of equation {sol1} and {sol2}")
dighat()
