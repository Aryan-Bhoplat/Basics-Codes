n = int(input("Enter a number:"))

if n<2 :
    print()

else:
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("prime")

    else:
        print("not prime")
        
