#задача 24.

n = int(input("Сколько у фермера кустов? "))
a = [int(i) for i in input("Сколько уродилось на каждом? ").split()][:n]
max_harvest = 0

for i in range(1, len(a) - 1):
    if max_harvest < a[i] + a[i - 1] + a[i + 1]:
        max_harvest = a[i] + a[i - 1] + a[i + 1]

if max_harvest < a[0] + a[len(a) - 1] + a[1]:
    max_harvest = a[0] + a[len(a) - 1] + a[1]

if max_harvest < a[0] + a[len(a) - 1] + a[len(a) - 2]:
    max_harvest = a[0] + a[len(a) - 1] + a[len(a) - 2]

print(f"Максимальный сбор за 1 раз {max_harvest}")
