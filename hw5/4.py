""" ✔ Создайте функцию генератор чисел Фибоначчи
"""


def fib():
    f1, f2 = 0, 1
    while True:
        f1, f2 = f2, f1 + f2
        yield f1


fib_num = fib()
for _ in range(40):
    print(next(fib_num), end=' ')
