
'''
l2 = [1,1,2,3,4,5,4,6]
l1 =[]

for items in l2:
    if items not in l1:
        l1.append(items)

print(l1)
'''

list1 = []

for i in range(5):
    value = input(f"Enter value {i+1}:")
    list1.append(value)

l2 = []
for item in list1:
    if item not in l2:
        l2.append(item)
        
print(l2)