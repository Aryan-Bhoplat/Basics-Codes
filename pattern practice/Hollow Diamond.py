n = int(input("Enter a number:"))
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        if k == 0 or k == 2*i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n-1,0,-1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        if k == 0 or k == 2*i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

'''
n = int(input("Enter a num:"))
for i in range(1, n+1):
    print(' '*(n-i), end='')
    for k in range(2 * i - 1):
        print('^' if k == 0 or k == (2*i-2) else ' ',end='')
    print()
for i in range(n-1,0,-1):
    print(' '*(n-i), end='')
    for k in range(2 * i - 1):
        print('^' if k == 0 or k == (2*i-2) else ' ',end='')
    print()
'''