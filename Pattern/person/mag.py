from rpg.Pattern.person.Hero_pattern import Hero


class Mag(Hero):
    """Класс мага (наследует героя)"""

    def __init__(self, name='маг', live=100, mana=0, power=1, knack=1, intel=5, exp=0, level=1, weapon='палочка'):
        """((Имя, здоровье, мана), сила, ловкость, интеллект, опыт, уровень)"""
        super().__init__(name, live, mana, power, knack, intel, exp, level)
        self.thisSpells = []
        self.Pack.thisPack['палочка'] = 10
        self.thisWeapon = {weapon, self.Pack.thisPack[weapon]}

    def scream(self):
        """Вывод сообщения мага"""
        return f'Я маг герой {self.thisName} и я знаю {len(self.thisSpells)} заклинаний'

    def add_magic(self, magic):
        """Добавление новых заклинаний"""
        self.thisExp += 10
        if self.thisExp == 100:
            self.thisPower += 1
            self.thisKnack += 2
            self.thisIntel += 4
            self.thisExp = 0

        self.thisSpells.append(magic)
        print(f'{magic} добавлен в список заклинаний')
