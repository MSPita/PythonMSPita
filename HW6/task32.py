maxim = int(input("Максимум диапазона: "))
minim = int(input("Минимум диапазона: "))
list_1 = [int(i) for i in input().split()]
for i in range(len(list_1)):
    if minim <= list_1[i] <= maxim:
        print(i, end=' ')