x,y,z = map(int, input("Enter 3 values:").split())

if z == y == z:
    print("All values are same.",x)
elif x>y and x>z:
    print(x,"is greatest")
elif y>x and y>z:
    print(y,"is greatest")
else:
    print(z,"is greatest")