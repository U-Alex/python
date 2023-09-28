""" Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
    У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
    Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""


class Animal:
    #count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #Animal.count += 1

    def show_unique(self):
        return 'no data'


class Dog(Animal):
    def __init__(self, name, age, commands_list: list = None):
        super().__init__(name, age)
        self.commands_list = [] if (commands_list is None) else commands_list

    def show_unique(self):
        commands = f"not trained" if len(self.commands_list) == 0 else \
            f"executes commands: {', '.join(self.commands_list)}"
        return commands


class Cat(Animal):
    def __init__(self, name, age, wool_length: int = 10):
        super().__init__(name, age)
        self.wool_length = wool_length

    def show_unique(self):
        coat = 'shorthair' if self.wool_length < 10 else 'long-haired'
        return f"coat type: {coat}"


class Bird(Animal):
    def __init__(self, name, age, flight_altitude: int = 0):
        super().__init__(name, age)
        self.flight_altitude = flight_altitude

    def show_unique(self):
        return f"flight altitude: {self.flight_altitude} m"


if __name__ == '__main__':
    pet1 = Dog('бобик', 3, ['лежать', 'голос'])
    pet2 = Cat('васька', 3, 11)
    pet3 = Bird('кеша', 3, 8)

    for pet in [pet1, pet2, pet3]:
        print(f"{pet.__class__.__name__} - {pet.name} - {pet.show_unique()}")

    #print(f"total pets: {Animal.count}")