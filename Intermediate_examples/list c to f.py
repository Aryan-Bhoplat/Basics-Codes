temp_c = list(map(int ,input("Enter temp in Celsius:").split()))
print("\nTemperature in Celsius:",temp_c)
temp_f =[]
for temp in temp_c:
    f = (temp * (9/5))+32

    temp_f.append(f)

print("Temperature in Farenheit:",temp_f)