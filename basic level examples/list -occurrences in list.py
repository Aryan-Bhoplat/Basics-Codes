my_list = [1,2,3,1,1,4,5,3,5,4,2,2]
target = 4
count = 0

for item in my_list:
    if item == target:
        count += 1

print(count)