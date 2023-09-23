""" Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""

import json
from typing import Callable
from random_csv import create_csv

param_list = []


def multi_quad(*, rows_count: int = 100):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            global param_list
            param_list = create_csv(rows_count)
            res_list = []
            for param in param_list:
                res_list.append(func(*list(map(int, param))))
            # return list(zip(param_list, res_list))
            return res_list

        return wrapper

    return deco


def save_result(*, filename: str = 'result.json'):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            # param_list = read_csv()
            result = func(*args, **kwargs)
            create_json(result, filename)
            return ['результаты сохранены в файл']

        return wrapper

    return deco


def create_json(result, filename):
    global param_list
    res_json = list()
    for item in zip(param_list, result):
        res_json.append([{'parameters': list(map(int, item[0]))}, {'roots': item[1]}])
    with open(filename, 'w', encoding='UTF-8') as f_json:
        json.dump(res_json, f_json, indent=2)


"""
def read_csv():
    param_list = []
    with open('random.csv', 'r', newline='') as f:
        for csv_file in csv.reader(f):
            param_list.append(csv_file)
    return param_list
"""
