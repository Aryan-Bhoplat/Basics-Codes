import random

def guess_num():
    guess_value = random.randint(1, 10)
    attempts = 3
    print("Let's play a guessing game.Guess a number between 1-10(3 tries only):")

    for i in range(attempts):
        guess = int(input(f"\nAttempt-({i+1}):"))
        if guess == guess_value:
            print("Congrats!")
        else:
            print("Try again.")
    print("\nHAHA, LOOSER. Correct ans was:",guess_value)
        
guess_num()