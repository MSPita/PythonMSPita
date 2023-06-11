a1 = int(input("Первый элемент прогрессии: "))
d = int(input("Разность прогрессии: "))
n = int(input("Количество элементов прогрессии: "))
a_n = []
for i in range(n):
    a_n.append(a1+i*d)
    
print(*a_n)