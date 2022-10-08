# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:1

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import os
os.system('cls' if os.name == 'nt' else 'clear')
min=1
max=10

def random_my(min,max):
    lets = set()
    list_1 = []
    for i in range(min,max):
        lets.add(str(i))
    for e in lets:
        list_1.append(int(e))
    return list_1
list_1=random_my(min,max)
sum_1 = 0 
for i in range(len(list_1)):
    if i % 2 !=0 and i != 0:
        sum_1+=list_1[i]
print(sum_1)
