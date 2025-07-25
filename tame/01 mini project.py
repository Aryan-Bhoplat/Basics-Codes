# Calculator 
while True:
    print('''
        ====Calculator====
        «Options»
        
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit
        ''')
    
    try:
        choice = int(input("Enter your choice:"))

        if choice == 5:
            print("Exiting the calculator")
            break

        a,b = map(int, input("Enter 2 numbers:").split())


        if choice == 1:
            print(f"Addition: {a+b}")
        elif choice == 2:
            print(f"Subtraction: {a-b}")
        elif choice == 3:
            print(f"Multiplication: {a*b}")
        elif choice == 4:
            if b == 0:
                print("Error 404.")
            else:
                print(f"Division: {a/b}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please input valid choice.")