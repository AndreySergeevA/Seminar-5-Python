# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

s = ''
n = int(input())
while n > 0:
    s = s + str(n % 2)
    n //= 2
print(s[::-1])