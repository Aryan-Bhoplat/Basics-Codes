# Write a function to return the sum of all numbers in a list.

l1 = [1,2,3,4,5,6,7,8,9]

def sum_inlist():
    sum = 0
    for i in l1:
        sum+=i
    print(sum)
        
sum_inlist()