# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input("Введите длину массива: "))
a = [int(i) for i in input("Задайте элементы массива: ").split()]

x = int(input("Введите число для сравнения: "))
# count = 0
for arg in a:
    if x == arg:
        count += 1
  
print(count)