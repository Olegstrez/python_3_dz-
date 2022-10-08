# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением др1обной части элементов.

# Пример:
# 1
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
lst = [round(random.uniform(0,10),2) for i in (range(random.randint(2,6)))]
random.shuffle(lst)
print(f"Исходный список:\n {lst}")
new_lst_1=[]
for i in lst:
    new_lst_1.append(round(i % 1,2))
result=max(new_lst_1)-min(new_lst_1)
print(f"Разница {round(result,2)}")
123

    
