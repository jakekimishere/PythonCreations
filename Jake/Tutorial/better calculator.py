num1 = float(input("Enter how many bitches you have: "))
operator = input("Enter if you want to multiply or add or subtract or divide bitches (+/-): ")
num2 = float(input("Enter how many bitches you think you have: "))

if operator== "+":
    print(num1+num2)
elif operator== "-":
    print(num1 - num2)
elif operator== "/":
    print(num1 / num2)
elif operator == "*":
    print(num1*num2)
else:
    print("choose either * + - or /")


