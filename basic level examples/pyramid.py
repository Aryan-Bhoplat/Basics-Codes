n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    '''ex : 5-1 = 4
            5-2 = 3 and so on
    '''
    for space in range(n - i):
        print(" ", end="")
    
    # Print stars
    for star in range(2 * i - 1):
        print("*", end="")
    
    # Move to next line
    print()
