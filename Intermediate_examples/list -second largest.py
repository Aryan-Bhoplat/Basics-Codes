'''
l1 = [9,2,4,5,2,6,4,8,4,5]
l1 = sorted(set(l1))

print(f"{l1[-2]}")
'''

'''
l1 = [9,2,4,5,2,6,4,8,4,5]
largest = max(l1)
second = float('-inf')
for num in l1:
    if num !=largest and num > second:
        second = num
print(second)
'''

l1 = [9,2,4,5,2,6,4,8,4,5]
first = float('-inf')
second = float('-inf')

for num in l1:
    if num > first:
        second = first
        first = num
    elif num != first and num > second:
        second = num
print(second)


        


    