"""Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
Пример:
Для n=4 -> [2, 2.25, 2.37, 2.44]
Сумма 9.06
"""

n = int(input('Введите количество элементов: '))
elem_list = []
sum = 0
for i in range(1, n + 1):
    elem = (1 + 1 / i) ** i
    elem_list.append(round(elem, 2))
    sum += elem
print(elem_list)
print(f'сумма: {round(sum, 2)}')
