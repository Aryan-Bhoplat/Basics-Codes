# if string contains any digits
'''
s = input("String:")
digits = "0123456789"

found = False
for char in s:
    if char in digits:
        found = True
        break

if found:
    print("It contains digit.")
else:
    print("It does not contain any digit.")
'''

# count vowels and consonant

''' 
s = input("String:")
vowels = 'aeiouAEIOU'

vowel_count = 0
consonant_count = 0

for i in s:
    if i.isalpha():
        if i in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print(vowel_count)
print(consonant_count)
'''
# upper and lowercase
'''
s = input("string:")

s1 = s.upper()
s2 = s.lower()

print(s1)
print(s2)
'''
# replace spaces

'''
s = input("string:")

s1 = s.replace(" ", "")
print(s1)
'''

#replace vowels 
'''
s = input("string:")
vowels = 'aeiouAEIOU'

for char in vowels:
    s = s.replace(char,"*")
    

print(s)
'''
#frequency
'''
s = input("string:")

freq = {}

for char in s:
    if char == " ":
        continue
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

for key in freq:
    print(f"{key}: {freq[key]}")
'''

#remove symbols
'''
import string

s = input("string:")
result = ""

for char in s:
    if char not in string.punctuation:
        result+=char

print(result)
'''