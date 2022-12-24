
import random

def degree_to_utf(degree):
    indexes = { "0": "\u2070", "1": "\u00B9", "2": "\u00B2", "3": "\u00B3", "4": "\u2074",
                "5": "\u2075", "6": "\u2076", "7": "\u2077", "8": "\u2078", "9": "\u2079", "-": "\u207B"}
    d_string = ''
    for num in str(degree):
        d_string += indexes[num]
    return d_string

def utf_to_degree(str_utf):
    indexes = { "\u2070": "0", "\u00B9": "1", "\u00B2": "2", "\u00B3": "3", "\u2074": "4",
                "\u2075": "5", "\u2076": "6", "\u2077": "7", "\u2078": "8", "\u2079": "9", "\u207B": "-"}
    degree = ''
    for num in str(str_utf):
        degree += indexes[num]
    return int(degree)

def str_to_dict(str_line):
    el_list = str_line.replace(' ', '').replace('=0', '').replace('-', ' -').replace('+', ' +').strip().split(' ')
    el_dict = {}
    for el in el_list:
        str_kf = el.split('x')
        if str_kf[0] in ['', '-', '+']:
            str_kf[0] += '1'
        if len(str_kf) == 1:    degree = 0
        elif str_kf[1] == '':   degree = 1
        else:
            if str_kf[1].startswith('**'):
                degree = int(str_kf[1].split('**')[1])
            else:
                degree = utf_to_degree(str_kf[1])
            
        el_dict[degree] = int(str_kf[0])
    return el_dict

def dict_to_str(el_dict, utf=False):
    str_line = ''
    for key, val in el_dict.items():
        if val == 0:        continue#pass
        elif val == 1:      str_line += '+'
        elif val == -1:     str_line += '-'
        elif val < -1:      str_line += '-' + str(-val)
        else:               str_line += '+' + str(val)
        if key == 0:        pass
        elif key == 1:      str_line += 'x'
        else:           
            if utf:    
                str_line += 'x' + degree_to_utf(key)
            else:
                str_line += 'x**' + str(key)

    str_line = str_line.replace('-', ' - ').replace('+', ' + ').replace(' ', '', 2) + ' = 0'
    if str_line.startswith('+'):
        str_line = str_line.replace('+', '', 1)
    return str_line

def create_dict(k :int, start, stop):
    el_dct = {}
    for deg in range(k, -1, -1):
        el_dct[deg] = random.randint(start, stop)
    return el_dct

def str_to_file(str_line, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(str_line)
    return

def file_to_str(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        str_line = file.read()
    return str_line

def sum_dict(d1: dict, d2: dict):
    d3 = {}
    for key, d1_val in d1.items():
        d2_val = d2.get(key, None)
        if d2_val != None:
            d3[key] = d2_val + d1_val
            del d2[key]
    d1.update(d2)
    d1.update(d3)
    return dict(sorted(d1.items(), reverse=True, key=lambda x: x[0]))

k1 = int(input('введите степень первого многочлена: '))
k2 = int(input('введите степень второго многочлена: '))
el_dict1 = create_dict(k1, -100, 100)
el_dict2 = create_dict(k2, -100, 100)
str_line1 = dict_to_str(el_dict1, True)
str_line2 = dict_to_str(el_dict2, True)
str_to_file(str_line1, 'file1.txt')
str_to_file(str_line2, 'file2.txt')
print('первый многочлен: ' + str_line1 + '  записан в file1.txt')
print('второй многочлен: ' + str_line2 + '  записан в file2.txt')
print('вычисление суммы: чтение из file1.txt и file2.txt')
el_dict1 = str_to_dict(file_to_str('file1.txt'))
el_dict2 = str_to_dict(file_to_str('file2.txt'))
el_dict3 = sum_dict(el_dict1, el_dict2)
str_line3 = dict_to_str(el_dict3, True)
str_to_file(str_line3, 'file3.txt')
print('третий многочлен: ' + str_line3 + '  записан в file3.txt')





