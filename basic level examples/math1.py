n = int(input("Enter a number:"))

last_digit = n % 100
remaining_digits = n // 100

print(last_digit)
print(remaining_digits)