from decimal import Decimal

from parameters import Param
from user import User


class Session:
    """
    класс для операций вычисления, все основные расчеты выполняются тут
    использует класс parameters и экземпляр класса User
    """
    def __init__(self, user_name, logger):
        self.logger = logger
        self.user = User(user_name, self.logger)
        self.param = Param()

    def show_user(self):
        return self.user

    def is_new_user(self) -> bool:
        return self.user.new_user

    def round_money(self, user_sum):
        res = int(user_sum // self.param.multiplicity * self.param.multiplicity)
        return res if res != 0 else self.param.multiplicity

    def top_up(self, user_sum):
        if self.is_dispossession():
            self.dispossession()
        self.user.add_money(user_sum)
        self.bonus_transaction()
        self.logger.info(f'{self.user.name} top_up success')

    def bonus_transaction(self):
        if self.user.transactions_count >= self.param.transactions_count:
            self.user.transactions_count = 0
            percent = self.user.get_money() * self.param.transactions_interest / 100
            self.user.add_money(percent, bonus=True)

    def is_bonus_transactions(self):
        if not self.user.transactions_count:
            return [self.param.transactions_interest, self.param.transactions_count]
        return False

    def take_off(self, user_sum):
        percent = user_sum * self.param.withdrawal_interest / 100
        if percent < self.param.withdrawal_min:
            percent = self.param.withdrawal_min
        if percent > self.param.withdrawal_max:
            percent = self.param.withdrawal_max
        disp = self.is_dispossession()
        if self.user.get_money() < user_sum + percent + (disp[1] if disp else 0):
            self.logger.warning(f'{self.user.name} не достаточно средств на счете ({self.user.get_money()} < {user_sum + percent + (disp[1] if disp else 0)})')
            raise Warning('не достаточно средств на счете')
        if disp:
            self.dispossession()
        self.user.sub_money(user_sum + percent)
        self.bonus_transaction()
        self.logger.info(f'{self.user.name} take_off success')
        return percent

    def dispossession(self):
        percent = self.user.get_money() * self.param.dispossession_interest / 100
        self.user.sub_money(percent, bonus=True)

    def is_dispossession(self):
        if self.user.get_money() >= self.param.dispossession_threshold:
            percent = self.user.get_money() * self.param.dispossession_interest / 100
            return [self.param.dispossession_interest, percent.quantize(Decimal("1.00"))]
        return False
