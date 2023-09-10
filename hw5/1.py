""" ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
    Для проверки числа на простоту используйте правило: «число является простым, если делится
    нацело только на единицу и на себя».
"""


def simple_gen(n):
    for num in range(2, n):
        if num % 2:
            simple = True
            for _tmp in range(3, num//2+1, 2):
                if not num % _tmp:
                    simple = False
                    break
            if simple:
                yield num


print([i for i in simple_gen(30)])
