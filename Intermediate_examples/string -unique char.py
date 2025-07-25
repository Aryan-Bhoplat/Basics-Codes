s = input("String:")
s = s.replace(' ','')
seen = set()
for char in s:
    if char not in seen:
        print(char, end='')
        seen.add(char)
