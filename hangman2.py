def hangmanGame():
    def hangman7():
        print("__________________")
        print("--------")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")

    def hangman6():
        print("__________________")
        print("--------")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")

    def hangman5():
        print("__________________")
        print("--------")
        print("|      O")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("_")
    
    def hangman4():
        print("__________________")
        print("--------")
        print("|      O")
        print("|      |")
        print("|      |")
        print("|")
        print("|")
        print("_")
    def hangman3():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|")
        print("|      |")
        print("|")
        print("|")
        print("_")

    def hangman2():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|")
        print("|")
        print("_")
    def hangman1():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|     /")
        print("|")
        print("_")
    def hangman0():        
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|     / \\")
        print("|")
        print("_")
    hangmanWord = "whiteboard"
    linesOfChar = ""
    for char in hangmanWord:
        linesOfChar += "_ "

    triesLeft = 7
    guessedLetters = []

    print(f"Let's play Hangman! Guess the word:{linesOfChar}")
    print(f"Tries left: {triesLeft}")
    hangman7()




    while triesLeft > 0:
        #Take an input letter and convert it to lowercase
        guessedLetter = input('Guess a letter: ').lower()

        if guessedLetter in guessedLetters:
            print("You already guessed that letter!")
        elif guessedLetter in hangmanWord:
            print("Good guess!")
            guessedLetters.append(guessedLetter)
        else:
            print("Wrong guess!")
            triesLeft -= 1
        showWord = ""
        for char in hangmanWord:
            if char in guessedLetters:
                showWord += char + " "
            else:
                showWord += "_ "

        print(showWord)

        if all(char in guessedLetters for char in hangmanWord):
            print("Congratulations! You won!")
            break

        print("Tries left:", triesLeft)
        
    else:
        hangman0()
        print("You lost! The word was:", hangmanWord)


hangmanGame()