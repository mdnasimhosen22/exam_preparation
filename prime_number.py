# ফাংশন বানালাম - কোনো Number prime কিনা দেখবে
def is_prime(number):
    if number <= 1:
        return False  # ১ বা তার কম হলে prime না

    # ২ theke number niye vag kore dekhbe
    for i in range(2, number):
        if number % i == 0:
            return False   # ভাগ গেলে prime না

    return True  # কোথাও ভাগ না গেলে prime
# ইউজার থেকে ইনপুট নেওয়া
num = int(input("Enter your Number =  "))
# ফাংশন দিয়ে চেক করলাম
if is_prime(num):
    print(num, "Prime Number")
else:
    print(num, "Not Prime number")

# other Rules
def check_prime():
    num = int(input("Enter your Number =  "))  # ইনপুট ফাংশনের ভিতরেই নেওয়া

    if num <= 1:
        print(num, "Not prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print(num, "Not prime")
            return

    print(num, "Prime Number")

# function call


check_prime()


#class use kore prime number ber korbo sei programme


class prime_num:
    def __init__(self):
        num = int(input("Enter your Number =  "))  # ইনপুট ফাংশনের ভিতরেই নেওয়া
        if num <= 1:
            print(num, "Not prime")
            return

        for i in range(2, num):
            if num % i == 0:
                print(num, "Not prime")
                return

        print(num, "Prime Number")


prime_num()

# or
class PrimeNum:
    def __init__(self):
        self.num = int(input("Enter your number: "))

    def __str__(self):
        if self.num <= 1:
            return f"{self.num} Not prime"
        for i in range(2, self.num):
            if self.num % i == 0:
                return f"{self.num} Not prime"
        return f"{self.num} Prime Number"

# এখন print করতে হবে


print(PrimeNum())