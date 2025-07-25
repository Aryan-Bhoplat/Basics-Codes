
while True:
    try:
        a, b = map(int, input("Enter two numbers:").split())


        if b == 0:
            print("Division by zero is not possible.")
        else:
            print(f"Division: {a/b:.2f}")
            break

    except ValueError:
        print("Invalid")