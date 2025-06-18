# use fucntion
def find_factorial():
    num = int(input("Enter a number to find factorial: "))

    if num < 0:
        print("Factorial does not exist for negative numbers.")

    result = 1
    for i in range(1, num + 1):
        result *= i

    print(f"Factorial of {num} is {result}")

# function call
find_factorial()


# use class
class Factorial:
    def __init__(self):
        num = int(input("Enter a number to find factorial: "))

        if num < 0:
            print("Factorial does not exist for negative numbers.")

        result = 1
        for i in range(1, num + 1):
            result *= i

        print(f"Factorial of {num} is {result}")

# function call
find_factorial()

# or
class Factorial:
    def find_factorial(self):
        num = int(input("Enter a number to find factorial: "))

        if num < 0:
            print("Factorial does not exist for negative numbers.")
            return

        result = 1
        for i in range(1, num + 1):
            result *= i

        print(f"Factorial of {num} is {result}")


# Create object and call the method
obj = Factorial()
obj.find_factorial()
