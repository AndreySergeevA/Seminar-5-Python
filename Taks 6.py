# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('Task 6.txt', 'r', encoding='utf-8') as file:
    arr = file.readlines()
    arr = [int(i) for i in arr[0].split()]
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i - 1]:
            print((arr[i - 1] + arr[i]) // 2)