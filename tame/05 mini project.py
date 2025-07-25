l1 = [int(input(f"Enter value {i+1}:")) for i in range(5)]
largest = second = float('-inf')
for i in l1:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
        
print(largest)
print(second)