"""Напишите функцию для транспонирования матрицы
"""


def print_mtx(mtx: list[list]):
    for i in mtx:
        for j in i:
            print(j, end='\t')
        print()
    print()


def trans_mtx(mtx: list[list]) -> list[list]:
    # n_mtx = list()
    # for _ in range(len(mtx[0])):
    #    n_mtx.append([None for _ in range(len(mtx))])
    # for i in range(len(mtx)):
    #    for j in range(len(mtx[i])):
    #        n_mtx[j][i] = mtx[i][j]
    n_mtx = [[mtx[i][j] for i in range(len(mtx))] for j in range(len(mtx[0]))]

    return n_mtx


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print_mtx(matrix)
    matrix = trans_mtx(matrix)
    print_mtx(matrix)
    matrix = trans_mtx(matrix)
    print_mtx(matrix)
