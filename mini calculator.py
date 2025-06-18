# ei code ta chaile bad dite paris exam e lagbe na eta optional programme

# make the calculator
first_num = int(input("Enter the first number :"))
oparetor = input("Enter the oparetor (+ - * / % )")
second_num = int(input("Enter the second number :"))

if oparetor == "+":
    print(f"This result ({first_num} + {second_num}) = ",first_num+second_num)
elif oparetor == "-":
    print(f"This result ({first_num} - {second_num}) = ",first_num-second_num)
elif oparetor == "*":
    print(f"This result ({first_num} * {second_num}) = ",first_num*second_num)
elif oparetor == "/":
    print(f"This result ({first_num} / {second_num}) = ",first_num/second_num)
elif oparetor == "%":
    print(f"This result ({first_num} % {second_num}) = ",first_num%second_num)
else:
    print("Error math")

# calculator make the python function
def car():
    first_num = int(input("Enter the first number :"))
    oparetor = input("Enter the oparetor (+ - * / % )")
    second_num = int(input("Enter the second number :"))
    if oparetor == "+":
        print(f"This result ({first_num} + {second_num}) = ", first_num + second_num)
    elif oparetor == "-":
        print(f"This result ({first_num} - {second_num}) = ", first_num - second_num)
    elif oparetor == "*":
        print(f"This result ({first_num} * {second_num}) = ", first_num * second_num)
    elif oparetor == "/":
        print(f"This result ({first_num} / {second_num}) = ", first_num / second_num)
    elif oparetor == "%":
        print(f"This result ({first_num} % {second_num}) = ", first_num % second_num)
    else:
        print("Error math")
car()

# calculator make to python function 
def cal():
    if oparetor == oparetor:
        return num_1 + num_2
    elif oparetor == oparetor:
        return num_1 - num_2
    elif oparetor == oparetor:
        return num_1 * num_2
    elif oparetor == oparetor:
        return num_1 / num_2
    elif oparetor == oparetor:
        return num_1 % num_2
    else:
        return "Error"

num_1 = int(input("Eeter the first number :"))
oparetor = input("Enter the oparetor (+ - * / % ) =")
num_2 = int(input("Eeter the second number : "))
print(f" This result of ({num_2} {oparetor} {num_2}) = ",cal())



