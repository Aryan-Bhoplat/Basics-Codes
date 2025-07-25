import random

def guess_num():
    guess_value = random.randint(1, 10)
    guess = int(input("Enter your guess:"))

    if guess == guess_value:
        print("Congrats!")
    else:
        print("Looser.")
    
    print("Correct ans:",guess_value)

guess_num()
