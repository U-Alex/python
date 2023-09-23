"""Генерация csv файла с тремя случайными числами в каждой строке"""

import csv
from random import randint


def create_csv(rows_count: int = 100):
    rows = []
    for i in range(rows_count):
        rows.append([randint(-100, 100) for _ in range(3)])
    with open('random.csv', 'w', newline='', encoding='utf-8') as f_scv:
        csv_write = csv.writer(f_scv, dialect='excel')
        csv_write.writerows(rows)

    return rows


if __name__ == '__main__':
    create_csv(10)
