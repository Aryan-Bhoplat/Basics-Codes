n = int(input("Enter a no.:"))

if n%3 == 0 and n%5 == 0:
    print("Fizzbuzz.",n,"is multiple of both 3 and 5")
elif n%3 == 0:
    print("Fizz.",n,"is multiple of 3")
elif n%5 ==0 :
    print("Buzz.",n,"is multiple of 5")
else:
    print("Multiple of none")
