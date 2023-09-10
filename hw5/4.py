""" ✔ Создайте функцию генератор чисел Фибоначчи
"""


def fib():
    f1 = 0
    f2 = 1
    while True:
        fs = f1 + f2
        f1 = f2
        f2 = fs
        yield f1


fib_num = fib()
for _ in range(40):
    print(next(fib_num), end=' ')
