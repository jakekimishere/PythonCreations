secret = "baggu"
guess =  ""
guessCount = 0
guessLimit = 10
nomoGuesses = False


while guess !=secret and not (nomoGuesses):
    print("Hint: He's gay")
    if guessCount < guessLimit:
      guess = input("Enter Guess: ")
      guessCount += 1
    else:
        nomoGuesses = True
if nomoGuesses:
    print("Yo lose")
else:
    print("Knew you were smart!")
