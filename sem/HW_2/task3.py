""" Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
    максимум использование библиотеки Random для и получения случайного int
"""
from random import randint

count = 100
num_list = [i for i in range(count)]
print(f'исходный список из {count} элементов int:\n{num_list}\n')

for i in range(count):
    j = randint(0, count-1)
    temp = num_list[i]
    num_list[i] = num_list[j]
    num_list[j] = temp

print(f'перемешанный список:\n{num_list}\n')
