while True:
    try:
        num = int(input("Enter a number:"))

        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} is divisible by both 3 and 5")
        elif num % 3 == 0 and num % 5!=0:
            print(f"{num} is divisible by 3 but not 5")
        elif num % 3 != 0 and num % 5==0:
            print(f"{num} is divisible by 5 but not 3")
        else:
            print(f"{num} is neither divisible by 3 nor 5")
    except ValueError:
        print("Invalid input.")