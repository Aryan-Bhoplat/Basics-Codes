'''
l1 = []
sum = 0
for i in range(10):
    value = int(input(f"Enter value {i+1}:"))
    l1.append(value)
    sum+=value
print(l1)
print("Sum of elements in list is equal to",sum)
'''

#Or


value = list(map(int, input(f"Enter value :").split()))

total = sum(value)
print(value)
print("Sum of elements in list is equal to",total)

