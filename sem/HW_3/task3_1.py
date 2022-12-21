""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
    Пример:
    [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

def trans(num):
    return round(num % 1, 2)

lst = [1.1, 1.2, 3.1, 5, 10.01]
max = trans(lst[0])
min = trans(lst[0])

for num in lst:
    num = trans(num)
    if num != 0:
        max = num if (num > max) else max
        min = num if (num < min) else min

result = max - min
print(f'{lst} => {result}')