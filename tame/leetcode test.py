def two_sum(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]

num = [4,3,56,7,5,3,2,3,6,7,8,9]
target = 9
print(two_sum(num, target))