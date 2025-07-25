list1 = []
new_list = []
for i in range(5):
    value = int(input(f"Enter value {i+1}:"))
    list1.append(value)

for num in list1:
    if num > 0:
        new_list.append(num)
        

print(new_list)