import json
import os


class User:
    users_dir = 'users'

    def __init__(self, name):
        self.name = name
        self.new_user = False
        self.money = 0
        self.transactions_count = 0
        self.loading()

    def __str__(self):
        return f"клиент: {self.name}, средств на счете: {self.money} у.е."

    def loading(self):
        try:
            f_name = os.path.join(self.users_dir, f"{self.name}.json")
            with open(f_name, 'r', encoding='utf-8') as f_json:
                self.__dict__ = json.load(f_json)
        except IOError as err:
            self.saving()
            self.new_user = True

    def saving(self):
        f_name = os.path.join(self.users_dir, f"{self.name}.json")
        with open(f_name, 'w', encoding='UTF-8') as f_json:
            json.dump(self.__dict__, f_json, indent=4)

    def add_money(self, user_sum, bonus=False):
        if not bonus:
            self.transactions_count += 1
        self.money += user_sum
        self.saving()

    def sub_money(self, user_sum, bonus=False):
        if not bonus:
            self.transactions_count += 1
        self.money -= user_sum
        self.saving()


