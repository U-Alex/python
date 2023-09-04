""" Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
    ✔ Какие вещи взяли все три друга
    ✔ Какие вещи уникальны, есть только у одного друга
    ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
    ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

source_dict = {'Вася': ('палатка', 'топор', 'кастрюля', 'дрова', 'спирт', 'мясо', 'кружки'),
               'Петя': ('палатка', 'лопата', 'кастрюля', 'дрова', 'спирт', 'мясо'),
               'Саша': ('палатка', 'топор', 'кастрюля', 'дрова', 'спирт', 'вода', 'нож'),
               }
friends = len(source_dict.keys())
list_1, list_2, list_3 = set(), set(), set()
str_3 = 'есть у всех, кроме: '
list_all = []

for key, val in source_dict.items():
    list_1 = list_1 & set(val) if len(list_1) else set(val)
    list_all.extend(val)
print(f"все друзья взяли: {', '.join(list_1)}")

for val in list_all:
    if list_all.count(val) == 1:
        list_2.add(val)
    if list_all.count(val) == friends - 1:
        list_3.add(val)
print(f"уникальные вещи: {', '.join(list_2)}")

for key, val in source_dict.items():
    _tmp = list_3.difference(val)
    if len(_tmp):
        str_3 += f"{key} -> {''.join(_tmp)}, "
print(str_3)














