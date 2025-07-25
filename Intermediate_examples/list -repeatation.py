l1 = [2,5,3,1,6,7,9,7,5,3,3,1,4,9]
l1 = sorted(l1)

freq = {}

for num in l1:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1

print(freq)