n = int(input())
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        if k == 0 or k == 2*i - 2 or i == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Or
'''
n = int(input("Enter a num:"))
for i in range(1, n+1):
    print(' '*(n-i), end='')
    
    for k in range(2 * i - 1):
        print('^' if k == 0 or k == (2*i-2) or i == n else ' ',end='')
        
    print()
'''
"""
n = 5
for i in range(1, n+1):
    for j in range(1,2*n):
        if j == n-i+1 or j == n+i-1 or i==n:
            print("*", end="")
        elif n-i+1 < j < n+i-1:
            print("+", end="")   
        else:
            print(" ", end="")
    print()
"""