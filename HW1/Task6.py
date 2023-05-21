print("Ваш билет счастливый?") 
print("Введите шестизначный номер билета: ")
a = int(input())

n = int(a//1000)
sum1 = 0
while n>0:
    i = n%10
    sum1 = sum1 + i
    n = n//10

m = int(a%1000)
sum2 = 0
while m>0:
    j = m%10
    sum2 = sum2 + j
    m = m//10

if sum1 == sum2:
    print ("Yes")
else:
    print ("No")    