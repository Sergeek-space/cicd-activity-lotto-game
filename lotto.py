#!/usr/bin/env python3

"""Lotto Game. 
Maintainer me@sergeek.space
"""

import os
import sys
import random

# Screen clear function
def screen_clear():
   # for Mac OS and linux (here, os.name is 'posix')
   if os.name == "posix":
      _ = os.system("clear")
   else:
      # for Windows
      _ = os.system("cls")

screen_clear()

# Define a number of games and fetch user's choice
games = [10, 50, 100] # in $
counter = 1
print("Play LOTTO: \n")
for game in games:
    print(f"To play for ${game} press {counter}")
    counter += 1
print ("To escape press 0")
user_input = int(input("> "))

# Define prises: each prise twice lesser than the previous one
# One attempt for each prise, 3 attempts in total.
if user_input > len(games):
    sys.exit("Nonexisting game! Exiting")
if user_input == 0:
    sys.exit("Game ended")

prises = []
prise1 = games[user_input - 1]
prises.append(prise1)
prise2 = prise1 // 2
prises.append(prise2)
prise3 = prise2 // 2
prises.append(prise3)

screen_clear()

# Define the game rules and fetch user's choice
game_rules = f"""Computer will generate a random number between 1 and 10,
and you have {len(prises)} chanses to guess.
"""

counter = 1
for x in range(len(prises)):
    game_rules += "\nIf you guess from the " + str(counter) + " attempt, you will get $" + str(prises[x])
    counter += 1

print(game_rules)

random_number = random.randint(1, 10)
#print(random_number)

attempts = len(prises)
counter = 1
while attempts:
    user_attempt = int(input( "Attempt number " + str(counter) + ". Type your answer: "))
    if(user_attempt == random_number):
        print(f"Congratulations! You win ${str(prises[counter - 1])}.")
        break
    if(user_attempt < random_number):
        print("Your number is smaller.")
        attempts -= 1
        counter += 1
    if(user_attempt > random_number):
        print("Your number is bigger.")
        attempts -= 1
        counter += 1
    if(attempts == 0):
        print(f"The number was {random_number}. You lost!")

#TODO: Loop the game: Again(A) or Exit(E)