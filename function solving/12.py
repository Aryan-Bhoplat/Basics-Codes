def no_of_digits(num):
    count = 0
    for digit in str(num):
        count+=1
    return count
while True:
    try:
        z = int(input("Enter a number:"))
        c = no_of_digits(z)
        print(f"Number of digits in integer:{c}")
    except ValueError:
        print("Invalid input")
