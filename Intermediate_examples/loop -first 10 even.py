'''
print("First 10 even numbers:")
for i in range(1,21):
    if i % 2 == 0:
        print(i, end=" ")
print()
'''

#Or

def first_evens():
    print("First 10 even numbers:")
    for i in range(1,21):
        if i % 2 == 0:
            print(i, end=" ")
    print()

first_evens()
    
    
