""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
    Пример:
    [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
import random

def process(my_list):
    odd_list = []
    sum = 0
    for i in range(1, len(my_list), 2):
        odd_list.append(my_list[i])
        sum += my_list[i]
    return odd_list, sum

my_list = []
for _ in range(12):
    my_list.append(random.randint(0, 10))

odd_list, sum = process(my_list)
odd_list_f = f"{', '.join(map(str, odd_list[:-1]))} и {str(odd_list[-1])}"

print(f"{my_list} -> на нечётных позициях элементы {odd_list_f}. ответ: {sum}")
