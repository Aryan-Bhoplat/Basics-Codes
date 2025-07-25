
def head_line():
    print('''
        ==Temperature converter==

        «Options»
        1. Celsius to Farenheit.
        2. Farenheit to Celsius.''')

def your_choice(choice):
    try:
        if choice== '1':
            temp_cel = float(input("Enter temp(celsius):"))
            temp_faren = temp_cel*(9/5)+32
            print(f"Temperatur in farenheit is:{temp_faren:.2f}")
            return temp_faren
        elif choice== '2':
            temp_faren = float(input("Enter temp(farenheit):"))
            temp_cel = (temp_faren-32)*(5/9)
            print(f"Temperature in celsius is:{temp_cel:.2f}")
            return temp_cel
        else:
            print("Please select option 1 or 2.")
    except ValueError:
        print("Invalid.")
        
def main():
    while True: 
        head_line()
        choice = input("Enter your choice(1 or 2) or press q to quit:")
        if choice.lower() == 'q':
            print("Exit")
            break
        
        your_choice(choice)

main()


        
