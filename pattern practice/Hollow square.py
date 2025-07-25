n = 4

for i in range(1,n+1):
    for j in range(n):
        if j == 0 or j == n-1  or i == 1 or i == n:
            print("* ",end='')
        else:
            print("  ",end='')
    print("")