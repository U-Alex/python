# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def input_num():
    ok = False
    while not ok:
        try:
            coord = int(input('введите номер четверти: '))
            if coord > 0 and coord < 5:
                ok = True
        except:
            pass
    return coord

coord_list = ['x(0, +∞), y(0, +∞)', 
              'x(-∞, 0), y(0, +∞)', 
              'x(-∞, 0), y(-∞, 0)', 
              'x(0, +∞), y(-∞, 0)'
              ]
num = input_num()

print(f'диапазон возможных координат точек в {num} четверти: {coord_list[num-1]}')
