"""
for num in range(2,101):
    is_prime=True
    for i in range(2, int(num **0.5)+1):
        if num %i ==0:
            is_prime= False
            break
    if is_prime:
        print(num)    
"""
n = int(input("Max r:"))
for num in range (2,n+1):
    for i in range (2, int(num**0.5) +1):
        if num % i == 0:
            break
    else:
        print(num)