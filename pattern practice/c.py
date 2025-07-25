'''
n = 5
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

#Or

n = 5

for i in range(1, n+1):
    for j in range(n+1):
        if i == j or j == (n+1)-i:
            print("x", end=' ')
        else:
            print(" ",end=' ')
    print()