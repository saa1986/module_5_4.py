class House:
    houses_history = []  # Атрибут класса для хранения названий домов

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)  # Добавляем название дома в историю

    @classmethod
    def new(cls, *args):
        # Создание нового объекта House и добавление его имени в историю
        if len(args) < 2:
            raise ValueError("Необходимо указать название и количество этажей.")
        name = args[0]
        number_of_floors = args[1]
        return cls(name, number_of_floors)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House.new('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House.new('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
del h1  # ЖК Эльбрус снесён, но он останется в истории