'''
num = int(input("Enter a number:"))

for i in range(1,11):
    result = num*i
    print(f"{num} x {i} = {result}")
'''

#Or

def mult(num):
    for i in range(1,11):
        result = num*i
        print(f"{num} x {i} = {result}")
    
while True:
    try:
        z = int(input("Enter a number:"))
        mult(z)
        
    except ValueError:
        print("Invalid.")


