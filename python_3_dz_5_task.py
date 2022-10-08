# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 1
import os
os.system('cls' if os.name == 'nt' else 'clear')

def fibanachi(number_2):
    list_1=[0,1,1]
    list_2=[-1,1]
    for i in range(3,number_2+1):
        z = list_1[i-2]+list_1[i-1]
        list_1.append(z)
        if i % 2 == 1:
            z1=z*(-1)
            list_2.insert(0, z1)
    for i in range(0,number_2+1):
        list_2.append(list_1[i])
    return list_2
print(fibanachi(10))
        





