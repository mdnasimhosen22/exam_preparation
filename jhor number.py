# use function
def even_numbers():
    for i in range(1,101):
        if (i%2 == 0):
            print(f"This number {i} is even number")
even_numbers()

# use class
class EvenNumbers:
    def print_evens(self):
        for num in range(1, 101):
            if num % 2 == 0:
                print(f"Evev Number {num}")

obj = EvenNumbers()
obj.print_evens()

