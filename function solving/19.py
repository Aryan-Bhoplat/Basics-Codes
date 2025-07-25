def los(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i.capitalize())
    return new_lst
    
lst = input("List of strings:").split()
result = los(lst)
print(result)

        
