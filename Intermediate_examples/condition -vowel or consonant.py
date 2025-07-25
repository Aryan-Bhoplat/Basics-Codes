while True:
    s = input("Character:")
    vowels = 'aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vowels:
                print(f"{i} is a vowel.")
            else:
                print(f"{i} is a consonant.")
        else:
            print("Enter an alphabet.")