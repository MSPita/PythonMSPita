# Задача 14
n = int(input("Введите число: "))
i = 0
while 2 ** i <= n:
    print(2 ** i, end=' ')
    i += 1