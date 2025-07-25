def vowels_instring(s):
    vowels = 'aeiouAEIOU'
    count=0
    for i in s:
        if i in vowels:
            count+=1
    print(count)
            
vowels_instring(input("Enter a string:"))
