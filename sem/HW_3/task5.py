""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    Пример:
    для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
"""

def input_num():
    ok = False
    while not ok:
        try:
            coord = int(input('введите индекс: '))
            if coord > 0:
                ok = True
        except:
            pass
    return coord

def fib(k):
    lst = []
    f1 = 0; f2 = 1
    for i in range(k):
        fs = f1 - f2
        f1 = f2; f2 = fs
        lst.append(f1)
    lst.reverse()
    lst.append(0)
    f1 = 0; f2 = 1
    for i in range(k):
        fs = f1 + f2
        f1 = f2; f2 = fs
        lst.append(f1)
    return lst

fib_list = fib(input_num())

print(f'список чисел Фибоначчи:\n{fib_list}')
