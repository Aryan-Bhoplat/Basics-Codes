'''
def sort_lst(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)

    merged = l1 + l2
    xi = sorted(merged)
    return xi

l1 = input("Enter elements of 1st list:")    
l2 = input("Enter elements of 2nd list:")  

c = sort_lst(l1, l2)
print(c)
'''

#Or

def sort_lst(s1, s2):
    merged = s1 + s2
    unique_lst = sorted(set(merged), key = lambda x: x.lower())

    return unique_lst

s1 = list(input("Elements of list 1:").replace(' ',''))
s2 = list(input("Elements of list 2:").replace(' ',''))

result = sort_lst(s1, s2)
print(result)