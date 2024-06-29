import os
import pickle


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} покушал')


class Bird(Animal):
    def __init__(self, name, age, feathers_color):
        super().__init__(name, age)
        self.color = feathers_color

    def make_sound(self):
        if self.age < 2:
            print(f'{self.name} сказал "Пи-Пи-Пи-Пи"')
        else:
            print(f'{self.name} сказал: "Курлык-Курлык-Курлык"')


class Mammal(Animal):
    def __init__(self, name, age, weight, fur_color):
        super().__init__(name, age)
        self.weight = weight
        self.color = fur_color

    def make_sound(self):
        if self.age < 2:
            print(f'{self.name} сказал "рр'
                  f'-рр-рр-рр"')
        else:
            print(f'{self.name} сказал: "РРР-РРР-РРР"')

    def eat(self):
        return f'{self.name} сьел {self.weight * 0.1} кг'


class Reptile(Animal):
    def __init__(self, name, age, length, scale_color):
        super().__init__(name, age)
        self.length = length
        self.color = scale_color

    def make_sound(self):
        print(f'{self.name} прошуршал всем телом длинной {self.length} метр')


class Zookeeper:
    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education

    def feed_animal(self, animal):
        print(f'Кормлю животное {animal.name}')


class Veterinarian:
    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education

    def health_animal(self, animal):
        print(f'Лечу живоное {animal.name}')


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        ''' Добавление одного или нескольких животных в зоопарк'''
        if len(animal) == 1:
            self.animals.append(animal)
        else:
            self.animals.extend(animal)

    def add_staff(self, staff):
        ''' Добавление одного или нескольких работников в зоопарк'''
        if len(staff) == 1:
            self.staff.append(staff)
        else:
            self.staff.extend(staff)

    def animal_sound(self, animal_object):
        ''' Звук животного'''
        print(f'  {animal_object.color} ', end='')
        animal_object.make_sound()

    def animal_sounds(self, animals_tmp):
        ''' Список звуков всех животных в зоопарке'''
        print('Звуки животных:')
        for animal_type in animals_tmp:
            self.animal_sound(animal_type)

    def print_animals(self):
        ''' Распечатка списка животных'''
        print(f'Список животных:')
        for animal in self.animals:
            print(f'  Тип: {animal.name} '
                  f'Возраст(лет): {animal.age} '
                  f'Цвет {animal.color}')

    def print_staff(self):
        ''' Распечатка списка сотрудников'''
        print('Список сотрудников:')
        for worker in self.staff:
            print(f'  Имя: {worker.name} '
                  f'Возраст: {worker.age} '
                  f'Образование: {worker.education}')

    def save_zoo_info(self, file_name):
        ''' Сохранение экземпляра класса Zoo в файл'''
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)


FILE_NAME = 'zoo.pkl'

animals = [Bird('Попугай', 1, 'Зеленый'),
           Mammal('Корова', 5, 100, 'Белая'),
           Reptile('Питон', 2, 1, 'Пятнистый')]
staff_list = [Zookeeper('Петр Иванов', 34, 'Нет'),
              Zookeeper('Иван Петров', 23, 'Нет'),
              Zookeeper('Мария Сидорова', 45, 'Среднее'),
              Veterinarian('Карл Йохансон', 65, 'Высшее')]


def load_zoo_info(file_name):
    ''' Чтение из файла сохраненного экземпляра класса'''
    with open(file_name, 'rb') as f:
        zoo_tmp = pickle.load(f)
    return zoo_tmp


def main():
    full_path_filename = os.getcwd() + '\\' + FILE_NAME
    # Экземпляр класса Zoo
    zoo = Zoo()
    zoo.add_animal(animals)
    zoo.add_staff(staff_list)
    print('_____________________________________')
    print('Экземпляр класса Zoo - первоначальный')
    print('_____________________________________')
    zoo.print_animals()
    zoo.print_staff()
    zoo.animal_sounds(zoo.animals)
    zoo.save_zoo_info(full_path_filename)
    # Экземпляр класса Zoo считанный из файла
    zoo_read = load_zoo_info(full_path_filename)
    print('_____________________________________')
    print('Экземпляр класса Zoo - считанный из файла')
    print('_____________________________________')
    zoo_read.print_animals()
    zoo_read.print_staff()
    zoo.animal_sounds(zoo.animals)


if __name__ == '__main__':
    main()
