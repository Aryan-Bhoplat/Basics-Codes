'''
a, b = map(int, input("Enter two numbers with one space:").split())

print(f"Before:-> a:{a} and b:{b}")
a, b = b, a
print(f"After:-> a:{a} and b:{b}")
'''

#Or

def swapping(a,b):
    print(f"Before:-> a:{a} and b:{b}")
    a,b = b,a
    print(f"After:-> a:{a} and b:{b}")
swapping(3,7)
