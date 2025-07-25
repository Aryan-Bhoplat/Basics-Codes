'''
year = int(input("Enter a year:"))

if year % 4 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year")
'''

#Or

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year")

leap_year(int(input("Enter a year:")))