sum = 0
count = 0
while True:
    try:
        n = int(input("N:"))
        sum+=n
        if n ==0:
            break
        count+=1
    except ValueError:
        print("Invalid.")
print("Sum:",sum)
print("Number of inputs:",count)