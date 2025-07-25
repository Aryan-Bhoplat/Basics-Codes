'''
def mult(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

z = int(input("Enter a number:"))
mult(z)
'''

#Or 

def mult(num):
    [print(f"{num} x {i} = {num * i}") for i in range(1,11)]

z = int(input("Enter a number:"))
mult(z)