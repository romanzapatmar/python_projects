# Project Name : Number Guessing Game in Python
# Author : Roman Zapatmar
# Date : 06 June 2025

# import random
# actualNo = random.randint(1, 100) #it can be random any no between 1 to 100
# actualNo = 83
# attempts = 0

# while True:
#     attempts += 1
#     guess = int(input("Guess the Number:\n"))
    
#     if guess < actualNo:
#         print("You guessed too low")
#     elif guess > actualNo:
#         print("You guessed too high")
#     else:
#         print(f"You guessed the right number in {attempts} attempts!")
#         break

# print("Thanks for playing the game!")

import random

number = random.randint(1, 100)
guess = None
attempts = 0

def get_hint(guess, number):
    diff = abs(guess - number)
    if diff == 0:
        return "Correct! 🎉"
    elif diff <= 3:
        return "🔥 Very Close!"
    elif diff <= 10:
        return "🙂 Close!"
    elif guess < number:
        return "❄️ Too Low and Far"
    else:
        return "🌋 Too High and Far"

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while guess != number:
    try:
        guess = int(input("Guess the number: "))
        attempts += 1
        print(get_hint(guess, number))
    except ValueError:
        print("Please enter a valid number.")

print(f"You guessed it in {attempts} attempts!")

