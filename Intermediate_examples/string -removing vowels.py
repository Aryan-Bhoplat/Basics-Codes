s = input("String:")
s = s.replace(' ','')
vowels = 'aeiouAEIOU'
for i in vowels:
    s = s.replace(i, '')
print(s)

