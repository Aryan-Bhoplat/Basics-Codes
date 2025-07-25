'''
num = int(input("Enter a number:"))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"Factorial of {num} is {fact}")
'''

#Or 

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

z = int(input("Enter a number:"))
c = factorial(z)
print(f"Factorial of {z} is {c}")



