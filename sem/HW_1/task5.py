"""    Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
def input_coord(txt):
    ok = False
    while not ok:
        try:
            coord = input(f'Введите координаты точки {txt} x,y (через запятую): ').split(',')
            if len(coord) == 2:
                res = [float(item) for item in coord]
                ok = True if (res[0] and res[1]) else False
        except:
            pass
    return res

def hypotenuse(x, y):
    return (x ** 2 + y ** 2) ** (0.5)

point_a = input_coord('A')
point_b = input_coord('B')
result = hypotenuse(point_a[0] - point_b[0], point_a[1] - point_b[1])

print(f'расстояние между точками: {round(result, 2)}')
