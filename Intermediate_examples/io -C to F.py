'''
def ctof(c):
    faren_ = c*(9/5)+32
    return faren_

z = ctof(float(input("Enter celsius value:")))
print("Farenheit:",z)
'''

#or

c = float(input("Enter celsius value:"))
temp_f = c*(9/5)+32

print(f"{temp_f:.2f}")