from decimal import Decimal


class Param:
    dispossession_threshold = Decimal(5_000_000)
    dispossession_interest = 10                 # налог на богатство

    multiplicity = 50                           # кратность

    transactions_interest = 3                   # процент за бонусную операцию
    transactions_count = 3                      # количество операций для начисления процента

    withdrawal_interest = 1.5                   # процент за снятие
    withdrawal_min = Decimal(30)                # минимальный процент за снятие
    withdrawal_max = Decimal(600)               # максимальный процент за снятие

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
