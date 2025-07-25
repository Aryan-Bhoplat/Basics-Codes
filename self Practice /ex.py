'''m1=input("enter movie1 name:")
m2=input("enter movie2 name:")
m3=input("enter movie3 name:")
m4=input("enter movie4 name:")
fav_mov=[]
fav_mov.append(m1)
fav_mov.append(m2)
fav_mov.append(m3)
fav_mov.append(m4)
print(fav_mov)
movie=fav_mov.copy()
movie.reverse()
if movie==fav_mov:
    print("is palindrome")
else:
    print("not palindrome")    
'''

l1 = []
n = int(input("Num:"))
for i in range(1, n+1):
    value = input(f"Value {i}:")
    l1.append(value)

print(l1)