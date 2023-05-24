# Задача 10

print ("сколько монеток на столе? ")
n = int(input ())
count = 0
count1 = 0
i = 1

while i <= n:
    x = int(input ("Орел (1) или решка (0)? "))
    
    if x == 1:
        count += 1
    else: 
        count1 += 1
    i += 1  

if count > count1:
    print (f'{count1} переверните')
else:
    print (f'{count} переверните')
