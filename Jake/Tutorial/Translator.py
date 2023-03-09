def translate(phrase):
    translation = ""
    for word in phrase:
        if word.lower() in "bed":
           translation = "rack"
        else:
            translation = translation + word
    return translation

print(translate(input("Enter a word: ")))

# this is a comment
'''
r
g
rgrg
er
'''
try:
    number = int(input("Enter a number "))
    print(number)
except  ZeroDivisionError:
    print("invalid input")
except ValueError:
    print("Wrong input")