
def long_word(s):
    
    longest = ''
    for i in s.split():
        if len(i) > len(longest):
            longest = i
        
    return longest, len(longest)
    

z = input("String:")
c, i = long_word(z)
print(f"Length of longest word:{i} and  word:{c}")