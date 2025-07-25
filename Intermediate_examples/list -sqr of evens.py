'''
l1 = []

for i in range(1,21):
    if i % 2 == 0:
        value = i ** 2
        l1.append(value)

print(l1)
'''

l1 = [i**2 for i in range(1,21) if i%2 ==0]
print(l1)