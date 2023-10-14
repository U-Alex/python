import logging
import re
from session import Session


class View:
    """
    класс взаимодействия с пользователем, запускает сессию для операций и сами операции
    """
    operations = {"m": "self.show_menu()",
                  "c": "self.show_user()",
                  "1": "self.top_up()",
                  "2": "self.take_off()",
                  "x": "self.set_filter()"
                  }
    menu = {"m": "показать главное меню",
            "c": "показать данные счета",
            "1": "пополнение счета",
            "2": "снятие со счета",
            "x": "выход"
            }

    def __init__(self, debug=False):
        self.session = None
        self.logger = logging.getLogger('bankomat')
        self.init_log(debug)

    def init_log(self, debug):
        self.logger.setLevel(logging.DEBUG if debug else logging.INFO)
        logger_handler = logging.FileHandler('logging.log', encoding='utf-8')
        logger_handler.setLevel(logging.DEBUG if debug else logging.INFO)
        logger_formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)
        self.logger.debug('Настройка логирования окончена!')

    def auth(self):
        while True:
            user_name = input('Авторизация... введите имя  (x - выход): ').title()
            if user_name in ['X', 'Х']:
                break
            pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ]{2,}$")
            if pattern.search(user_name):
                try:
                    self.logger.info(f'{user_name} login')
                    self.session = Session(user_name, self.logger)
                    print(f'добро пожаловать, {user_name}')
                    print('создан новый счет' if self.session.is_new_user() else 'загрузка данных счета...')
                    self.start()
                except IOError as err:
                    self.logger.critical(f'{user_name} (IOError) {err}')
                    print(f'ошибка ввода-вывода {err}\n дальнейшее выполнение невозможно')
                except (IndexError, KeyError) as err:
                    self.logger.critical(f'{user_name} (IndexError, KeyError) {err}')
                    print(f'внутренняя ошибка {err}\n дальнейшее выполнение невозможно')
                finally:
                    self.session = None
                    self.logger.info(f'{user_name} logout')
                    print(f'сессия пользователя {user_name} закончена\n')
            else:
                print('нужно ввести имя')
                continue

    def start(self):
        self.show_menu()
        while True:
            user_input = input("input operation: ")
            if user_input in ['X', 'Х', 'x', 'х']:
                break
            operation = self.operations.get(user_input, False)
            if operation:
                eval(operation)

    def show_menu(self):
        print('--- главное меню ---')
        for it, op in self.menu.items():
            print(f"{it} : {op}")

    def show_user(self):
        print('--- данные счета ---')
        print(self.session.show_user())

    def top_up(self):
        try:
            user_sum = self.session.round_money(abs(float(input("введите сумму пополнения: "))))
        except ValueError:
            print('неверный ввод, отмена операции')
            return
        print(f'сумма округлена до {user_sum}, пополнение...')
        if disp := self.session.is_dispossession():
            print(f"внимание! будет снято {disp[0]} процентов - {disp[1]} у.е. (налог на богатство)")
        self.session.top_up(user_sum)
        if perc := self.session.is_bonus_transactions():
            print(f"зачислено {perc[0]} процента за каждую {perc[1]} операцию")
        self.show_user()

    def take_off(self):
        try:
            user_sum = self.session.round_money(abs(float(input("введите сумму снятия: "))))
        except ValueError:
            print('неверный ввод, отмена операции')
            return
        print(f'сумма округлена до {user_sum}, снятие...')
        if disp := self.session.is_dispossession():
            print(f"внимание! будет снято {disp[0]} процентов - {disp[1]} у.е (налог на богатство)")
        try:
            perc_sum = self.session.take_off(user_sum)
            print(f"дополнительно снято: {perc_sum} у.е.")
            if perc := self.session.is_bonus_transactions():
                print(f"зачислено {perc[0]} процента за каждую {perc[1]} операцию")
        except Warning as warn:
            print(warn)
        self.show_user()


