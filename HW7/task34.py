# Задача 34:  Винни-Пух попросил Вас посмотреть, 
# ; есть ли в его стихах ритм. Поскольку разобраться 
# ; в его кричалках не настолько просто, насколько легко 
# ; он их придумывает, Вам стоит написать программу. 
# ; Винни-Пух считает, что ритм есть, если число слогов 
# ; (т.е. число гласных букв) в каждой фразе стихотворения
# ;  одинаковое. Фраза может состоять из одного слова, если 
# ;  во фразе несколько слов, то они разделяются дефисами. 
# ;  Фразы отделяются друг от друга пробелами. Стихотворение  
# ;  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите 
# ;  “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# ;  если с ритмом все не в порядке

verse = list(input("А есть ли ритм? Стих:  ").lower().split())
list_res = set()
for word in verse:
    count = 0
    for i in word:
        if i in "аяоёуюиыеэ":
            count += 1
    list_res.add(count)    

if len(list_res) == 1:
    print ('Парам пам-пам')
else:
    print('Пам парам')

 