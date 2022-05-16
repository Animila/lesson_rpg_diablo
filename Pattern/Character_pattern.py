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
        if self.thisLive >= 100:
            self.thisLive = 100
        print(f'Восстановлено здоровья: {potion}')

    def drink_mana_potion(self, potion_mana):
        """Использование зелья для восстановления манны"""
        self.thisMana += potion_mana
        if self.thisMana >= 100:
            self.thisMana = 100
        print(f'Восстановлено маны: {potion_mana}')
