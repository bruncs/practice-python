"""
  Exercise 9
"""
# pylint: disable=invalid-name

import random
playAgain = "y"

while playAgain == "y":
    tries = 0
    guess = int(input("\nGuess a number from 1 to 9: "))
    tries += 1
    number = random.randrange(1, 10)

    while guess != number:
        if guess < number:
            guess = int(input("Too low. Try again: "))
            tries += 1
        elif guess > number:
            guess = int(input("Too high. Try again: "))
            tries += 1

    print("\nYou guessed the number "+ str(number) +" with "+ str(tries) +" tries.")
    playAgain = input("Would you like to play again (y/n)? ")

print("\nThank you for playing!")
