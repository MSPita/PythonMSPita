# Задача 12

s = int(input("Сумма: "))
p = int(input("Произведение: "))
d = s**2 - 4*p

if d >= 0:
    x1 = (s + d**0.5)/2
    x2 = (s - d**0.5)/2
    print (x1, x2)
else:
    print ('Нет решения.')