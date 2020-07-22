# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
dashes = []
guesses = []
tries = 0


def make_dashes():
    for _ in word:
        dashes.append("-")


def update_dashes(letter):
    for l in range(len(word)):
        if letter == word[l]:
            dashes.pop(l)
            dashes.insert(l, letter)


def check_repeat(letter):
    return bool(letter in guesses)


def check_single(letter):
    return bool(len(letter) != 1)


def check_lower(letter):
    return bool(not letter.islower())


def reset():
    global word, dashes, guesses, tries
    word = random.choice(words)
    dashes = []
    guesses = []
    tries = 0
    make_dashes()


print("H A N G M A N")

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')

    if menu == "play":
        reset()
        while True:
            print()
            print("".join([str(elm) for elm in dashes]))
            guess = input("Input a letter: ")

            if check_single(guess):
                print("You should input a single letter")

            elif check_lower(guess):
                print("It is not an ASCII lowercase letter")

            elif check_repeat(guess):
                print("You already typed this letter")

            elif guess in word:
                update_dashes(guess)
                guesses.append(guess)
            else:
                print("No such letter in the word")
                tries += 1
                guesses.append(guess)

            if "".join([str(elm) for elm in dashes]) == word:
                print(f"You guessed the word {word}!\nYou survived!\n")
                break

            if tries == 8:
                print("You are hanged!\n")
                break
    elif menu == "exit":
        break
