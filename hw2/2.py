""" Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
    Программа должна возвращать сумму и произведение* дробей.
    Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction


def User_input(num_string):
    while True:
        user_str = input(f"введите строку {num_string} вида 'a/b' - дробь с числителем и знаменателем\n").split('/')
        if len(user_str) == 2 and user_str[0].isdigit() and user_str[1].isdigit():
            return int(user_str[0]), int(user_str[1])


def Reduction(a, b):
    """сокращение дроби"""
    fnd = a if a < b else b
    while fnd > 0:
        if a % fnd == 0 and b % fnd == 0:
            a /= fnd
            b /= fnd
        fnd -= 1
    return [int(a), int(b)]


def Sum_fr(a1, b1, a2, b2):
    b = b1 * b2
    a = a1 * (b / b1) + a2 * (b / b2)
    return Reduction(a, b)


def Mul_fr(a1, b1, a2, b2):
    return Reduction(a1 * a2, b1 * b2)


a1, b1 = User_input('1')
fract1 = Fraction(a1, b1)
a2, b2 = User_input('2')
fract2 = Fraction(a2, b2)

result_sum = Sum_fr(a1, b1, a2, b2)
result_mul = Mul_fr(a1, b1, a2, b2)

print()
print(f"{a1}/{b1} + {a2}/{b2} = {result_sum[0]}{'' if result_sum[1] == 1 else f'/{result_sum[1]}'}")
print(f"{a1}/{b1} * {a2}/{b2} = {result_mul[0]}{'' if result_mul[1] == 1 else f'/{result_mul[1]}'}")

print()
print(f'{fract1} + {fract2} = {fract1 + fract2}')
print(f'{fract1} * {fract2} = {fract1 * fract2}')

