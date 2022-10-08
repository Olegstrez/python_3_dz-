# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:1

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math
import os
os.system('cls' if os.name == 'nt' else 'clear')
min=0
max=10

def random_my(min,max,numbers):
    lets = set()
    list_1 = []
    count=0
    for i in range(min,max):
        lets.add(str(i))
        count+=1
        if count>=numbers:
            break
    for e in lets:
        list_1.append(int(e))
    return list_1
list_1=random_my(min,max,5)
print(list_1)
new_list=[]
for i in range(math.ceil(len(list_1)/2)):
    new_list.append(list_1[i]*list_1[-i-1])

print(new_list)


