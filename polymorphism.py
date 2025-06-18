# base class
class Person:
    def __init__(self,name,profession):
        self.nam = name
        self.porf = profession

    def show_details(self):
        print(f"Name:{self.nam}")
        print(f"Profession:{self.porf}")

# Derived class (Child) /Create child class


class students(Person):
    def __init__(self,name,address,profession,roll):
        super().__init__(name,profession)
        self.addr = address
        self.roll = roll

    def show_details(self):
        print(f"Name:{self.nam}")
        print(f"Profession:{self.porf}")
        print(f"Address:{self.addr}")
        print(f"Roll:{self.roll}")


# Polymorphic function
def describe_person(Person):
    Person.show_details()

# ✅ Object create korte hobe


person1= Person("Nasim", "developer")
person2 = students("Raihan","pabns","student",1)

describe_person(person1)
print("---------------")
describe_person(person2)


