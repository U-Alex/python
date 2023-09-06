""" Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
    где ключ — значение переданного аргумента, а значение — имя аргумента.
    Если ключ не хешируем, используйте его строковое представление.
"""


def my_func(**kwargs) -> dict:
    print(kwargs)
    new_dict = {}
    for key, val in kwargs.items():
        if val.__hash__:    new_dict[val] = key
        else:               new_dict[str(val)] = key

    return new_dict


n_dict = my_func(key1='blabla', key2=[None], key3=(True, False), key4=3.14)
print(n_dict)

