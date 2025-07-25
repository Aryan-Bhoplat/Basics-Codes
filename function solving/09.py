import math

def arcircle(radius):
        area = math.pi*radius*radius
        return area 

while True:
        try:
            z = float(input("Enter the radius:"))
            if z < 0:
                print("Radius cannot be negative.")
                continue
            break
        except ValueError:
              print("Invalid input.")

c = arcircle(z)
print(f"Area: {c:.2f}")
                



    
