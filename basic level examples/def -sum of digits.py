def sum_of_digits(s):
    sum = 0
    for i in s:
        if i.isdigit():
            sum +=int(i)
    print(sum)

sum_of_digits(input("Enter a number:"))