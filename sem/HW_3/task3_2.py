""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
    Пример:
    [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import random

lst = []
for _ in range(12):
    ind = random.randint(0, 3)
    lst.append(round(random.uniform(0, 10), ind))

lst2 = []
for num in lst:
    num = round(num % 1, 3)
    if num != 0:
        lst2.append(num)

result = round(max(lst2) - min(lst2), 3)
print(f'{lst} => {result}')
