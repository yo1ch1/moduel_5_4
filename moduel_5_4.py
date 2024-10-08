class House:

    house_history = []


    def __new__(cls, *args, **kwargs):
            cls.house_history.append(args[0])
            return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.numbers_of_floors = number_of_floors


    def go_to(self, new_floor):
        int(new_floor)
        for floor_number in range(1, new_floor+1):
            if new_floor < self.numbers_of_floors or new_floor < 1:
                print(floor_number)
            else:
                print('"Такого этажа не существует"')
                break

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей:{self.numbers_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors == other


    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors < other


    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors <= other


    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors > other


    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors >= other


    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors != other


    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self


    def __radd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self


    def __iadd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self


    def __del__(self):
        print(f'"{self.name} снесён, но он останется в истории"')


h1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h2 = House('ЖК Акация', 20)
print(House.house_history)
h3 = House('ЖК Матрёшки', 20)
print(House.house_history)
# Удаление объектов
del h2
del h3

print(House.house_history)