while True:
    try :
        n = int(input("Enter your age:"))
        if n > 0:
            if n >= 18:
                print("Eligible for voting")
                break
            else:
                print("Not eligible for voting")
        else: 
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")
    
