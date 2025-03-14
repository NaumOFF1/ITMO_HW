class Soda:
    def __init__(self, type_soda=None):
        self.type_soda = type_soda
    
    def show_my_drink(self):
        if self.type_soda:
            print(f"Газировка и {self.type_soda}")
        else:
            print("Обычная газировка")

soda1 = Soda("Cola")
soda2 = Soda()

soda1.show_my_drink()
soda2.show_my_drink()
