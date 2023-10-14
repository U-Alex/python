from decimal import Decimal
from database import Orm


class User:
    users_dir = 'users'
    users_auth = []

    def __new__(cls, name, logger):
        if name in cls.users_auth:
            logger.error(f'{name} is already joined to the session')
            raise IndexError('пользователь уже присоединен к сессии')
        return super().__new__(cls)

    def __init__(self, name, logger):
        self.name = name
        self.logger = logger
        self.__class__.users_auth.append(name)
        self.new_user = False
        self.__money = Decimal('0.00')
        self.transactions_count = 0
        self.loading()

    def __del__(self):
        if self.name in self.users_auth:
            self.users_auth.remove(self.name)

    def __str__(self):
        return f"клиент: {self.name}, средств на счете: {self.__money.quantize(Decimal('1.00'))} у.е."

    def loading(self):
        try:
            load_dict = Orm.loading(self)
            load_dict['_User__money'] = Decimal(load_dict['_User__money']).quantize(Decimal("1.00"))
            self.__dict__.update(load_dict)
            self.new_user = False
        except IOError:
            self.saving()
            self.new_user = True
            self.logger.info(f'{self.name} new_user')

    def saving(self):
        save_dict = {"name": self.name,
                     "_User__money": str(self.__dict__['_User__money'].quantize(Decimal("1.00"))),
                     "transactions_count": self.transactions_count}
        Orm.saving(self, save_dict)

    def get_money(self) -> Decimal:
        return self.__money

    def add_money(self, user_sum, bonus=False):
        self.__money += user_sum
        if not bonus:
            self.transactions_count += 1
        self.saving()

    def sub_money(self, user_sum, bonus=False):
        self.__money -= user_sum
        if not bonus:
            self.transactions_count += 1
        self.saving()


