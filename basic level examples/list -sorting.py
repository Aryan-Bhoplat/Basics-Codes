list1 = []
for i in range(5):
    value = int(input(f"Enter value {i+1}:"))
    list1.append(value)

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[j] < list1[i]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)