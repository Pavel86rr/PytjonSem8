# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

print(f'Введите текст:')
data = (input())
print(data)

data = list(data.split())

data1 = list(data.pop())
data1 = [x.lower() for x in data1]

data2 = list(data.pop())
data2 = [x.lower() for x in data2]

data3 = list(data.pop())
data3 = [x.lower() for x in data3]

if (sum(map(lambda x : 1 if 'а' in x else 0, data1))) == (sum(map(lambda x : 1 if 'а' in x else 0, data2))) == (sum(map(lambda x : 1 if 'а' in x else 0, data3))):
    print(f'Парам пам-пам')
else:
    print(f'Пам парам')

