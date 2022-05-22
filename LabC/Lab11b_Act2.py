# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 2
# Date:         29 November 2021
#

import random as rand


def is_guess(guess, number):
    return guess == number


def is_greater(guess, number):
    return guess > number


def is_less(guess, number):
    return guess < number


def main():
    # Generate number
    number = rand.randint(1, 100)
    print("Guess the secret number! Hint: it’s an integer between 1 and 100...")

    # Guess
    guess = 0
    num_guess = 0

    # Loop until guess correctly
    while guess != number:
        guess = int(input("What is your guess? "))

        # Guess correctly so immediately break
        if is_guess(guess, number):
            break

        # Guess is too large
        if is_greater(guess, number):
            print("Too high!")

        # Guess is too small
        if is_less(guess, number):
            print("Too low!")

        # Increase count
        num_guess += 1

    # Print the number of guesses
    print(f"You guessed it! It took you {num_guess} guesses.")


if __name__ == "__main__":
    main()
