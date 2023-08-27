""" Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
    Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
    Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

MIN = 1
MAX = 100000
def user_input():
    ok = False
    #num = None
    while not ok:
        try:
            num = int(input('Введите положительное число (не более 100000): '))
            if (num < MIN) or (num > MAX):
                raise Exception("неверное число")
            else:
                ok = True
        except Exception as error :
            print(error)
    return num

user_num = user_input()
simple = True
for num in range(2, user_num):
    if user_num % num == 0:
        simple = False
        break

result = "простое" if simple else "составное"
print(f"число {user_num} - {result} ")

