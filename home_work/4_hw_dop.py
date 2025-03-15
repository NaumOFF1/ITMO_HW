class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def starting_the_engine():
        print('Автомобиль заведен')

    def engine_shutdown():
        print('Автомобиль заглушен')

    def year_production(self):
        print(self.year)

    def type_auto(self):
        print(self.type)

    def color_auto(self):
        print(self.color)

bmw_3 = Car('Красный', 'Купе', '2022')

bmw_3.color_auto()