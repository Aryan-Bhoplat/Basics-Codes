n = int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    
    print("\r")

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    
    print("\r")

# Or

'''n = 5

for i in range(1, n+1):
    print(" "* (n-i) + "*" * (2*i-1) )
for i in range(n-1,0,-1):
    print(" "* (n-i) + "*" * (2*i-1) )
    
'''

'''
n = 5

for i in range(1,n+1):
    spaces = (n-i)*" "
    stars = (2*i-1)*"+"
    print(spaces+stars)
    
for i in range(n-1,0,-1):
    spaces = (n-i)*" "
    stars = (2*i-1)*"+"
    print(spaces+stars)
'''