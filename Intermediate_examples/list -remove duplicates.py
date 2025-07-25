'''
l1 = list(map(int, input("Enter list values:").split()))
print("Before:",l1)

l1 = sorted(list(set(l1)))
print("After:",l1)
'''
#Or

l1 = list(map(int, input("Enter list values:").split()))
print("Before:",l1)
print("\r")
l1 = sorted(l1)


freq = {}

for num in l1:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    if freq[key] > 1:
        print(f"{key} is repeated {freq[key]} times")
print("\r")

l1 = list(set(l1))
print("After:",l1)