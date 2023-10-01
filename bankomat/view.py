import re
from session import Session


class View:
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

    def __init__(self):
        self.session = None

    def auth(self):
        user_name = 'UAA'.title()  # input('введите имя: ').title()
        pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ]+$")
        if pattern.search(user_name):
            self.session = Session(user_name)
            print(f'добро пожаловать, {user_name}')
            print('создан новый счет' if self.session.is_new_user() else 'загрузка данных счета...')
            self.start()
        else:
            print('нужно ввести имя')
        print('сессия закончена')

    def start(self):
        self.show_menu()
        while True:
            user_input = input("input operation: ")
            if user_input == 'x':
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
        user_sum = self.session.round_money(float(input("введите сумму пополнения: ")))
        print(f'сумма округлена до {user_sum}, пополнение...')
        if disp := self.session.is_dispossession():
            print(f"внимание! будет снято {disp[0]} процентов - {disp[1]} у.е. (налог на богатство)")
        self.session.top_up(user_sum)
        if perc := self.session.is_bonus_transactions():
            print(f"зачислено {perc[0]} процента за каждую {perc[1]} операцию")

    def take_off(self):
        user_sum = self.session.round_money(float(input("введите сумму снятия: ")))
        print(f'сумма округлена до {user_sum}, снятие...')
        if disp := self.session.is_dispossession():
            print(f"внимание! будет снято {disp[0]} процентов - {disp[1]} у.е (налог на богатство)")
        try:
            perc_sum = self.session.take_off(user_sum)
            print(f"дополнительно снято: {perc_sum} у.е.")
            if perc := self.session.is_bonus_transactions():
                print(f"зачислено {perc[0]} процента за каждую {perc[1]} операцию")
        except Exception as err:
            print(err)



