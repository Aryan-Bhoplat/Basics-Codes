'''
x,y,z = map(int, input("Enter 3 no.:").split())

if x>y and x>z:
    print(f"{x} is greater.")
elif y>x and y>z:
    print(f"{y} is greater.")
else:
    print(f"{z} is greater.")
'''
#or

def largest(x,y,z):
    if x>y and x>z:
        print(f"{x} is greater.")
    elif y>x and y>z:
        print(f"{y} is greater.")
    else:
        print(f"{z} is greater.")

x,y,z = map(int, input("Enter 3 no.:").split())
largest(x,y,z)