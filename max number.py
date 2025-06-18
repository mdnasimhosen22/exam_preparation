
# 3 ti number er majhe sob cheye boro number ber korar hold programme
class max3num:                         # ✅ একটা class ঘোষণা করা হয়েছে যার নাম max3num
    def __init__(self):                # ✅ constructor method (__init__) ঘোষণা
        num1 = int(input("enter the first number = "))   # ইউজারের কাছ থেকে 1st সংখ্যা input নেয়া
        num2 = int(input("enter the second number = "))  # 2nd number
        num3 = int(input("enter the third number = "))   # 3rd  number

        # ✅ এখন চেক করা হয়েছে কোন number সবচেয়ে বড়
        if (num1 > num2) and (num1 > num3):
            print("maximum number = ", num1)
        elif (num2 > num1) and (num2 > num3):
            print("maximum number = ", num2)
        else:
            print("maximum number = ", num3)

# ✅ class er  constructor call, orthat object তৈরি ও init method চালানো
max3num()

#function use kore maximum nuber ber korar code

def maximum ():
    num1 = int(input("enter the first number = "))  # ইউজারের কাছ থেকে 1st সংখ্যা input নেয়া
    num2 = int(input("enter the second number = "))  # 2nd number
    num3 = int(input("enter the third number = "))  # 3rd  number

    # ✅ এখন চেক করা হয়েছে কোন number সবচেয়ে বড়
    if (num1 > num2) and (num1 > num3):
        print("maximum number =", num1)
    elif (num2 > num1) and (num2 > num3):
        print("maximum number = ", num2)
    else:
        print("maximum number = ", num3)
# function Invoked / call kora
max3num()



