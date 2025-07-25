'''
user_name = input("Enter your name:")
user_age = int(input("Enter your age:"))

future_age = user_age+5
print(f"In 5 years, {user_name} will {future_age} years old.")
'''
#Or

'''
def func(name, age):
    future_age = age+5
    print(f"In 5 years, {name} will be {future_age} years old.")

name, age = input("Enter your name and age:").split()
func(name, int(age))
'''
#Or

def func(name, age):
    future_age = age+5
    print(f"In 5 years, {name} will be {future_age} years old.")

name = input("Enter your name:")
age = int(input("Enter your age:"))
func(name, age)