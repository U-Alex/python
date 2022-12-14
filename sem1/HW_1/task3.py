"""     Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
        в которой находится эта точка (или на какой оси она находится).
    Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

def input_coord():
    ok = False
    while not ok:
        try:
            coord = input('Введите координаты точки x,y (через запятую): ').split(',')
            if len(coord) == 2:
                res = [float(item) for item in coord]
                ok = True if (res[0] and res[1]) else False
        except:
            pass
    return res

coord = input_coord()
x = coord[0]
y = coord[1]
if x > 0:
    num = 1 if (y > 0) else 4
else:
    num = 2 if (y > 0) else 3

print(f'номер четверти: {num}')