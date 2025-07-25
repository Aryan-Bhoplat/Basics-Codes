def sentence(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count+=1
    return count

z = sentence(input("String:"))
print(z)