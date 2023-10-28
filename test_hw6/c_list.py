class CustomList:
    def __new__(cls, data: list[int]):
        if isinstance(data, list) and all(map(lambda i: isinstance(i, int), data)):
            return super().__new__(cls)
        raise TypeError('неверный параметр ( list[int] )')

    def __init__(self, data: list[int]):
        self.data = data

    def __str__(self):
        return ', '.join(map(str, self.data))

    @property
    def average(self):
        return None if len(self.data) == 0 else sum(self.data) / len(self.data)

    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return self.average == other.average
    #     else:
    #         raise Exception(f'неверный класс ( CustomList )')


