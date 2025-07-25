def palin(s):
    s = s.lower().replace(" ","") 
    
    if s == s[::-1] :
        print("\nString is palindrome.\n")
    else:
        print("String is not palindrome")
    print("String:",s,"\nReversed string:",s[::-1])
        

c = input("String:")
palin(c)
