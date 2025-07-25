# Write a function that counts the number of vowels in a string.


def vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    count = 0

    for i in s:
        if i in vowels:
            count+=1
    print("Vowels:",count)
vowels_in_string("Hello World")