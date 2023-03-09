is_male = False
is_gay = True
if is_male and is_gay:
    print("You're gay")
elif is_male and not (is_gay):
    print("Love you bro")
elif not is_male and (is_gay):
    print("Love you bro")
else:
    print("you're def gay")

def maxNum(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        print("num1 is the winner")
        return num1
    elif num2 >= num1 and num2>= num3:
        print("num2 is the win")
        return num2
    else:
        print("num3 sucks! but won")
        return num3

print(maxNum(123, 46364, 45211))