while True:
    try:
        num = input("Enter a number:")
        num = num[::-1]
        se = int(num)
        break
        
    except ValueError:
        print("Invalid")
print("Reversed:",se)