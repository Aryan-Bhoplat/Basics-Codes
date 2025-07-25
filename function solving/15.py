def dunc(s):
    d1 = {}
    for items in s:
        if items in d1:
            d1[items] += 1
        else:
            d1[items] = 1
    return d1

z = input("String:")
c = dunc(z)
print(c)
    
