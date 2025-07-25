list1 = []

for i in range(5):
    value = int(input(f"Enter value {i+1}:"))
    list1.append(value)

count_even = 0
count_odd = 0
for num in list1:
    if num % 2 == 0:
        count_even +=1
    
    else:
        count_odd +=1
        
print("Even:",count_even)
print("Odd:",count_odd)