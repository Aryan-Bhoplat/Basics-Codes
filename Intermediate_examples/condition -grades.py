'''
marks = int(input("Enter your marks:"))

if 100 >= marks >=35:
    print("Pass ")
    if marks > 85:
        print('Grade-A')
    elif 85 >= marks > 70:
        print('Grade-B')
    elif 70 >= marks > 60:
        print('Grade-C')
    elif 60 >= marks >= 35:
        print('Grade-D')
elif marks < 35:
    print('Grade-Fail')
'''

#or

def marking(marks):
    if 100 >= marks >=35:
        print("Pass ")
        if marks > 85:
            print('Grade-A')
        elif 85 >= marks > 70:
            print('Grade-B')
        elif 70 >= marks > 60:
            print('Grade-C')
        elif 60 >= marks >= 35:
            print('Grade-D')
    elif marks < 35:
        print('Grade-Fail')
    return marks

marking(int(input("Enter your marks:")))