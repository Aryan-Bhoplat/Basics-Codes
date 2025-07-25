

def unique(l1):
    seen = set()
    result = []
    for i in l1:
        if i not in seen:
            seen.add(i)
            result.append(i)
            
    return result

z = input("Enter elements:")
c = unique(z)
print(c)