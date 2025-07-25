'''s = input("Enter a string:")
vowels = "aeiouAEIOU"

found = False
for char in s:
    if char in vowels:
        found = True
        break

if found:
    print("String contains vowel.")
else:
    print("String does not contain vowel.")
'''

s = input("Enter a string:")
vowels = "aA"

found = False
for char in s:
    if char in vowels:
        found = True
        break

if found:
    print("String contains a/A")
else:
    print("String does not contain a/A")