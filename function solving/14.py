'''
lst = [2, '4', 6.0, 3, None]

for num in lst:
    if isinstance(num, int): # example
        print(num, "is an integer")
'''


def even_sum(lst):
    sum = 0
    for value in lst:
        if isinstance(value, int) and value % 2 == 0:
            sum+=value

    return sum

z = map(int, input("Enter numbers in a list:").split())
c = even_sum(z)
print("Sum:",c)