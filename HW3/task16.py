# Задача 16: Требуется вычислить, сколько раз встречается 
#некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X


n = int(input("Введите длину массива: "))
a = [int(i) for i in input("Задайте элементы массива: ").split()]

x = int(input("Введите искомое число: "))
count = 0
for i in range(n):
    if x == a[i]:
        count += 1
  
print(count)