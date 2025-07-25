s = "Hello World!"
vowels = "aeiouAEIOU"
count = 0

found = False
for i in s:
    if i in vowels:
        count+=1

print("NO. of vowels:",count)
