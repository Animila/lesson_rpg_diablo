class Character:
    """Базовый персонаж"""

    def __init__(self, name, live, mana):
        """Имя, здоровье, опыт"""
        self.thisName = name
        self.thisLive = live
        self.thisMana = mana

    def Status(self):
        """Вывод состояния базового персонажа"""
        print('--<Статус персонажа:>--')
        print(f'\t>Имя: {self.thisName}')
        print(f'\t>Здоровье: {self.thisLive}')
        print(f'\t>Мана: {self.thisMana}')
        print('-----------------------')

    def drink_heal_poion(self, potion):
        """Проверка на ввод целых чисел для зелья здоровья"""
        pass

    def drink_mana_potion(self, potion_mana):
        """Проверка на ввод целых чисел для зелья маны"""
        pass
