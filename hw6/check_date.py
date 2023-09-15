""" ✔Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
    Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
    Для простоты договоримся, что год может быть в диапазоне [1, 9999].
    Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
    Проверку года на високосность вынести в отдельную защищённую функцию.
    В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
#from sys import argv


def valid_date(date_str: str) -> bool:
    max_num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _list = date_str.split('.')
    if len(_list) == 3 and _list[0].isdigit() and _list[1].isdigit() and _list[2].isdigit():
        _list = list(map(int, _list))
        if 0 < _list[2] < 10000:
            if _leap_year(_list[2]):
                max_num_days[1] = 29
            if (0 < _list[1] < 13) and (0 < _list[0] <= max_num_days[_list[1]-1]):
                return True
    """
    try:
        _list = date_str.split('.')
        _list[2] = ('000' + _list[2])[-4::]
        _date = datetime.strptime('.'.join(_list), '%d.%m.%Y')
    except ValueError:
        return False
    """
    return False


def _leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == '__main__':
    from sys import argv
    try:
        result = valid_date(argv[1])
        print("valid date" if result else "not valid date")
    except IndexError:
        print('требуется аргумент - дата в формате DD.MM.YYYY')
