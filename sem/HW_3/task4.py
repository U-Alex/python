""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    Пример:
    45 -> 101101
    3 -> 11
    2 -> 10
"""

def trans(num):
    str_bin = ''
    while num != 0:
        str_bin = str(num % 2) + str_bin
        num //= 2
    return str_bin

num = int(input('Введите положительное целое число: '))
str_bin = trans(num)

print(f'{num} -> {str_bin}')
