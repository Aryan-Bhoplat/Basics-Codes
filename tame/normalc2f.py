while True:
    print('''
        ==Temperature converter==

        «Options»
        1. Celsius to Farenheit.
        2. Farenheit to Celsius.''')

    choice = int(input("Enter your choice:"))
    if 0 < choice < 3:
        if choice== 1:
            temp_cel = int(input("Enter temp(celsius):"))
            temp_faren = temp_cel*(9/5)+32
            print("Temperatur in farenheit",temp_faren)
        else:
            temp_faren = int(input("Enter temp(farenheit):"))
            temp_cel = (temp_faren-32)*(5/9)
            print("Temperature in celsius",temp_cel)
    else:
        print("Please select option 1 or 2.")