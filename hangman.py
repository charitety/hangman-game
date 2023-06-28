#Importing Random-Word package 
#From https://pypi.org/project/Random-Word/
from random_word import RandomWords

r =RandomWords()

#Return a single random word
r.get_random_word()
#computer randomly generates a word
hangmanWord = r.get_random_word()

#player choses letter

#computer compares letter to word
def linesOfChar(word):
    linesOfChar =""
    for char in word:
        linesOfChar +="_ "
    return linesOfChar

hangmanWord = "whiteboard"
firstLine = linesOfChar(hangmanWord)
triesLeft = 7
while triesLeft <= 7: 
    guessedLetter = input("Enter a letter:").lower()
    if guessedLetter not in hangmanWord:
        triesLeft -= 1
        print("Oops! That letter is not correct!")
    else:
        print("Good guess!")
    if triesLeft == 0:
        print("You lose!")
        break
    
    lineGuessWord = f"Guess the word: {firstLine}"
    lineTriesLeft = f"Tries left: {triesLeft}"
    lineGuessLetter = f"Enter a letter:{guessedLetter}"
    lineGuess = ""

    print(lineGuessWord)
    print(lineTriesLeft)
    print(lineGuessLetter)
    print(lineGuess)

    def hangman1():
        print("__________________")
        print("--------")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")

    def hangman2():
        print("__________________")
        print("--------")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")

    def hangman3():
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
    def hangman5():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|")
        print("|      |")
        print("|")
        print("|")
        print("_")

    def hangman6():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|")
        print("|")
        print("_")
    def hangman6():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|     /")
        print("|")
        print("_")
    def hangman7():
        print("__________________")
        print("--------")
        print("|      O")
        print("|     \|/")
        print("|      |")
        print("|     / \\")
        print("|")
        print("_")
   
    
#if letter matches a character in random word, the word is revealed


# if tries in triesLeft print number of tries left

#if letter does not match computer draws body part
#computer iterates over entire word comparing to letter input
#if player reached 7 tries game over
#message:
#end of game displays result - win or loss
#enter letter: "Good Guess!"" if letter matches
#enter letter: "Oops! That letter is not correct!"
#characters: | - 0 \ /

#if guesses = 0
#print "--------"
#print "|      |"
#print "|      |"
#print "|      |"
#print "|      |"

# while tries > 0:
#   chan##         for letter in chosen_word:
#             if letter in guessed_letters:
#                 display_word += letter
#             else:
#                 display_word += 'lineofchar'
#         print(display_word)


#Stretch goals:
#Display a message if the input is not alphabetic
#Display a message if the user enters a letter twice "PARTIALLY ACHIEVED"
#Display a message if the user enters a wrong letter twice
#Add background colors to terminal print


