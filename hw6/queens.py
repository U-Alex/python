""" Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
    Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
    Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
    Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
    Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

    Напишите функцию в шахматный модуль.
    Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
    Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
from random import choice

_board = []


def _init_board():
    global _board
    _board = [['.' for _ in range(8)] for _ in range(8)]


def print_board():
    global _board
    for i in _board:
        for j in i:
            print(j, end='\t')
        print()
    print()


def _add_queen(crd: tuple = False) -> bool:
    global _board
    #print(f'{crd=}')
    _board[crd[0]][crd[1]] = '♕'
    _fil = {(i, crd[1]) for i in range(0, 8)}
    _fil.update({(crd[0], i) for i in range(0, 8)})
    _min = crd[0] if crd[0] < 7 - crd[1] else 7 - crd[1]
    _fil.update({(crd[0] - i, crd[1] + i) for i in range(1, _min + 1)})
    _min = 7 - crd[0] if 7 - crd[0] < 7 - crd[1] else 7 - crd[1]
    _fil.update({(crd[0] + i, crd[1] + i) for i in range(1, _min + 1)})
    _min = 7 - crd[0] if 7 - crd[0] < crd[1] else crd[1]
    _fil.update({(crd[0] + i, crd[1] - i) for i in range(1, _min + 1)})
    _min = crd[0] if crd[0] < crd[1] else crd[1]
    _fil.update({(crd[0] - i, crd[1] - i) for i in range(1, _min + 1)})
    for crd_f in _fil - {crd}:
        if _board[crd_f[0]][crd_f[1]] != '♕':
            _board[crd_f[0]][crd_f[1]] = 'ᴑ'
    #print(f'{_fil=}')


def check_queens(coords: list) -> bool:
    global _board
    _init_board()
    if len(coords) != 8:
        print("not 8")
        return False
    for crd in coords:
        if _board[crd[0]][crd[1]] != '.':
            return False
        _add_queen(crd)
    return True


def random_queens() -> bool:
    global _board
    _init_board()
    for num_queen in range(1, 9):
        _crds = []
        for i in range(8):
            for j in range(8):
                if _board[i][j] == '.':
                    _crds.append((i, j))
        if not len(_crds):
            return False
        _add_queen(choice(_crds))

    return True


#print(check_queens([(0,0), (2,3), (3,5), (1,6), (4,7), (5,1), (7,2), (6,4)]))
#print(random_queens())
#print_board()
