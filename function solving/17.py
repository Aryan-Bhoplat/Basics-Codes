def lp_year(year):
    if (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

while True:
    try:
        z = int(input("Enter a year:"))
        lp_year(z)
    except ValueError:
        print("Invalid input")
        
    
    


