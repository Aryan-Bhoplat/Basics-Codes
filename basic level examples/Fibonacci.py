n = int(input("Enter a no.:"))

a,b = 0,1

for i in range(n):
    print(a, end=' ')
    a,b = b, a+b
print()