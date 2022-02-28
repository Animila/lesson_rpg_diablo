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

    def drink_heal_potion(self, potion):
        """Использование зелья для восстановления жизни"""
        self.thisLive += potion

    def drink_mana_potion(self, potion_mana):
        """Использование зелья для восстановления манны"""
        self.thisMana += potion_mana