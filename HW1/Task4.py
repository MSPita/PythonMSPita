print("Сколько всего журавликов сделали дети? ")
s = int (input())
if s%6 == 0 and s >= 6:
    print('Петя сделал журавликов')
    print (int(s/6))
    print('Сережа сделал журавликов')
    print (int(s/6))
    print('Катя сделала журавликов')
    print (int(s/3*2))
else:
    print('Нет решения!')