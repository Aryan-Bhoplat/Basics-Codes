names = ['aryan','yash','om']
ages = [19,20,18]

combined = zip(names, ages)


l1 = [print(f"{name} is {age} years old.") for name, age in combined]
