""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    Пример:
    [2, 3, 4, 5, 6] => [12, 15, 16];
    [2, 3, 5, 6] => [12, 15]
"""
import random

def pairs(lst):
    len_lst = len(lst)
    m_lst = []
    for el in range(0, round(len(lst) / 2 + 0.5)):
        m_lst.append(lst[el] * lst[len_lst - el - 1])

    return m_lst

lst = []
for _ in range(random.randint(3, 8)):
    lst.append(random.randint(1, 8))

print(f'{lst} => {pairs(lst)}')

