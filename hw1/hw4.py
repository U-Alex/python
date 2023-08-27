""" угадывание числа
"""
from  random import randint

MIN = 0
MAX = 10
print(f'загадайте число от {MIN} до {MAX}')

def user_input():
    ok = False
    while not ok:
        user_inp = input('< , > , =  ')
        if user_inp in ['<', '>', '=']:
            ok = True
    return  user_inp

while True:
    num = randint(MIN, MAX)
    print('число', num)
    user = user_input()
    if user == '=':
        break
    elif user == '<':
        MAX = num - 1
    elif user == '>':
        MIN = num + 1
    #print('-', MIN, MAX)