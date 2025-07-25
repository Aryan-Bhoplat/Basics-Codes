s1 = input("Enter 1st string:").replace(' ','').lower()
s2 = input("Enter 2nd string:").replace(' ','').lower()

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("NO")