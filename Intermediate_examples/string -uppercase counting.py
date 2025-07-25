'''
s = input("String:")
count = 0

for i in s:
    if i.isupper():
        count+=1
print(count)
'''

#Or

s = input("String:")
count = sum(1 for i in s if i.isupper())
print("Uppercase letters:",count)