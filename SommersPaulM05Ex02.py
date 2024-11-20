"""
Author: Paul Sommers
Date written: 11/20/2024
Assignment: Module 05 Programming Assignment 2
Short Desc: This program generates a random number between 1 and 100 and asks the user to guess the number. 
            It replies if the guess is too high or too low, and congratulates the user when the guess the number.
            The game restarts with a new random number after a correct guess.
"""

import random

# Function to run the number guessing game
def numberGame():
    while True:
        # Generate a random number between 1 and 100
        randomNum = random.randint(1, 100)
        
        # Let the user to keep guessing until they guess the number
        while True:
            # Ask the user to guess
            guess = int(input("Guess a number (between 1 and 100): "))
            
            # Check if the guess is too high, too low, or correct
            if guess > randomNum:
                print("Too high!")
            elif guess < randomNum:
                print("Too low!")
            else:
                print("Nice! You guessed the number!")
                break  # Exit the inner loop and pick a new number

# Call the function to start the game
numberGame()