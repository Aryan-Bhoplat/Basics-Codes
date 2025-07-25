while True:
    try:
        def heat_conv(temp_c):
            temp_f = temp_c*(9/5)+32
            return temp_f
        z = float(input("Enter temperature: "))
        print(f"Celsius: {z}˚C")
        c = heat_conv(z)
        print(f"Farenheit: {c:.3f}˚F")
    except ValueError:
        print("Invalid input.")