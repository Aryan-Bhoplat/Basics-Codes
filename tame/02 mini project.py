# guessing

import random

print('''
      Let's start guessing game.
      Choose a number between 0-10.
      (User has 3 tries)''')

value = random.randint(0,10)

for i in range(3):
    print(f"Attempt-{i+1}» ")
    guess = int(input("Enter your guess:"))

    if guess < 0 or guess > 10:
        print("Invalid. Please enter value in valid range")
        continue
    
    if guess == value:
        print("Congrats, you win")
        break
    
    elif guess > value:
        print("Too high.")
    elif guess < value:
        print("Too low.")
else:
    print(f"Looser you loose, correct answer was {value}")
