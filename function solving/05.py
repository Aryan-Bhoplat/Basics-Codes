#Write a function to return the factorial of a number.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))