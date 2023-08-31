""" Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
    Функцию hex используйте для проверки своего результата.
"""

BASE = [16, '0x']
#BASE = [8, '0o']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
num = input("введите целое число: ")
if num.isdigit():
    new_num = []
    temp = int(num)
    while temp >= BASE[0]:
        new_num.append(digit_list[temp % BASE[0]])
        temp //= BASE[0]
    new_num.append(digit_list[temp % BASE[0]])
    new_num.reverse()
    print(f'{BASE[1]}{"".join(new_num)}')

    #проверка
    print(hex(int(num)))
    #print(oct(int(num)))
else:
    print("нужно ввести целое число")

