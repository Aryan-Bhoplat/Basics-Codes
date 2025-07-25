n = 47

for i in range(1,n+1):
    for spaces in range(n-i):
            print(" ",end="")

    for star in range(2*i-1):
          print("*",end="")

    print()

'''
n = 5

for i in range(1,n+1):
    spaces = (n-i)*" "
    stars = (2*i-1)*"+"
    print(spaces+stars)
'''

'''
n = 5

for i in range(1,n+1):
    print(' '*(n-i) + '^'*(2*i-1))
'''