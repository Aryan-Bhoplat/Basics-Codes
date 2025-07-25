'''
s = input("Enter a number:")
count = 0
for i in s:
    if i.isalpha():
        print("Invalid.")
        break
    else:
        count+=1

print(count)
'''

#or

while True:
    try:
        s = int(input("Enter a number:"))
        break

    except ValueError:
        print("Invalid.")
    
count = 0
for i in str(s):
    count+=1        
    
print(f"Number of digits in integer is/are:",count)
    
