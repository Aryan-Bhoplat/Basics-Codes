l1 = [] 
for i in range(5):
    while True:    
        try :
            value = int(input(f"Enter element {i+1}:"))
            l1.append(value)
            break
        except ValueError:
            print("Invalid input.")
print(l1) # To show list 
def largest(l1):
    max_value= l1[0]
    for i in l1:
        if i > max_value:
            max_value = i
    return max_value

print(f"{largest(l1)} is max value")


