from rpg.Pattern.person.Hero_pattern import Hero


class Warrior(Hero):
    """Класс воина (наследует героя)"""

    def __init__(self, name='воин', live=100, mana=0, power=5, knack=1, intel=1, exp=0, level=1):
        """((Имя, здоровье, мана), сила, ловкость, интеллект, опыт, уровень), оружие"""
        super().__init__(name, live, mana, power, knack, intel, exp, level)

    def scream(self):
        """Вывод сообщения о персонаже"""
        return f'Я герой {self.thisName} и я воин'
