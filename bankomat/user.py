import json
import os
from decimal import Decimal


class User:
    users_dir = 'users'
    users_auth = []

    def __init__(self, name):
        self.name = name
        if name in self.users_auth:
            raise Exception('пользователь уже присоединен к сессии')
        self.__class__.users_auth.append(name)
        self.new_user = False
        self.money = Decimal('0.00')
        self.transactions_count = 0
        self.loading()

    def __del__(self):
        if self.name in self.users_auth:
            self.users_auth.remove(self.name)

    def __str__(self):
        return f"клиент: {self.name}, средств на счете: {self.money.quantize(Decimal('1.00'))} у.е."

    def loading(self):
        try:
            f_name = os.path.join(self.users_dir, f"{self.name}.json")
            with open(f_name, 'r', encoding='utf-8') as f_json:
                load_dict = json.load(f_json)
            load_dict['money'] = Decimal(load_dict['money']).quantize(Decimal("1.00"))
            self.__dict__.update(load_dict)
            self.new_user = False
        except IOError:
            self.saving()
            self.new_user = True

    def saving(self):
        f_name = os.path.join(self.users_dir, f"{self.name}.json")
        save_dict = self.__dict__.copy()
        save_dict['money'] = str(save_dict['money'].quantize(Decimal("1.00")))
        save_dict.pop('new_user')
        with open(f_name, 'w', encoding='UTF-8') as f_json:
            json.dump(save_dict, f_json, indent=4)

    def add_money(self, user_sum, bonus=False):
        self.money += user_sum
        if not bonus:
            self.transactions_count += 1
        self.saving()

    def sub_money(self, user_sum, bonus=False):
        self.money -= user_sum
        if not bonus:
            self.transactions_count += 1
        self.saving()


