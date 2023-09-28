import math


class Triangle:
    def __init__(self, a, b, c):
        if (a < b + c) and (b < a + c) and (c < a + b):
            self.a, self.b, self.c = a, b, c
        else:
            raise Exception(f'неверные параметры')

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        pp = self.perimeter() / 2
        return math.sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c))


if __name__ == '__main__':
    args_list = [(1, 2, 3), (10.3, 10, 10), (3, 3, -1), (1, 3, 3)]
    figure_list = []
    for args in args_list:
        try:
            figure = Triangle(*args)
            figure_list.append(figure)
            print(f"Triangle({args}) -> perimeter = {figure.perimeter()}, area = {float.__round__(figure.area(), 3)}")
        except Exception as err:
            print(f"Triangle({args}) -> {err}")
