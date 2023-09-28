""" Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""

from Animals import *


class AnimalFab:
    def __init__(self):
        self.animal_list: list[Animal] = list()

    def new_animal(self, animal_type: str, name: str, age: int, unique=None) -> bool:
        if animal_type.lower() in ['dog', 'cat', 'bird']:
            self.animal_list.append(eval(animal_type.title())(name, age, unique))
            return True
        #raise...
        return False

    def get_all_list(self):
        return self.animal_list


if __name__ == '__main__':
    fab1 = AnimalFab()
    fab1.new_animal('dog', 'бобик', 3, ['лежать', 'голос'])
    fab1.new_animal('Dog', 'барбос', 3)
    fab1.new_animal('Cat', 'васька', 3, 11)
    fab1.new_animal('caT', 'люська', 3, 1)
    fab1.new_animal('BiRd', 'кеша', 3, 8)
    fab1.new_animal('Fish', '', 0, 0)

    for pet in fab1.get_all_list():
        print(f"{pet.__class__.__name__} - {pet.name} - {pet.show_unique()}")
