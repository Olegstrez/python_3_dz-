# Напишите программу, которая будет преобразовывать
#  десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# number_1=int(input("Ведите число = "))1
import os
os.system('cls' if os.name == 'nt' else 'clear')

def transfer_to_system(number_1):
    list_1=[]
    while True:
        if number_1 % 2 == 1 and number_1 !=2:
            list_1.append(1)
            number_1=(number_1-1)/2
        elif number_1 !=2:
            list_1.append(0)
            number_1=(number_1)/2
        if number_1 ==2:
            list_1.append(0)
            list_1.append(1)
            return list_1
        if number_1 ==1:
            list_1.append(1)
            return list_1
z = transfer_to_system(int(input("Ведите число = ")))
print("Перевод его в 2 систему")
print(z) 
     

