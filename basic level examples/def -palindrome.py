def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
    
is_palindrome(input("Enter a word:"))

