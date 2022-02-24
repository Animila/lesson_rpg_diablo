class Character:
    """Базовый персонаж"""

    def __init__(self, name, live, mana):
        """Имя, здоровье, опыт"""
        self.thisName = name
        self.thisLive = live
        self.thisMana = mana

    def Status(self):
        """Вывод состояния базового персонажа"""
        print('Статус персонажа:')
        print(f'\t>Имя: {self.thisName}')
        print(f'\t>Здоровье: {self.thisLive}')
        print(f'\t>Мана: {self.thisMana}')
        print('-----------------')

    def drink_heal_potion(self, potion):
        """Проверка на ввод целых чисел для зелья здоровья"""
        try:
            if int(potion) == float(potion):
                return True
            else:
                return 'Введено не целое число'
        except ValueError:
            return 'Неверный тип значения'

    def drink_mana_potion(self, potion_mana):
        """Проверка на ввод целых чисел для зелья маны"""
        try:
            if int(potion_mana) == float(potion_mana):
                return True
            else:
                return 'Введено не целое число'
        except ValueError:
            return 'Неверный тип значения'
