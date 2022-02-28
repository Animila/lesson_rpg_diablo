from rpg.Pattern.person.Hero_pattern import Hero


class Warrior(Hero):
    """Класс воина (наследует героя)"""

    def __init__(self, name='воин', live=100, mana=0, power=5, knack=1, intel=1, exp=0, level=1, weapon='кулак'):
        """((Имя, здоровье, мана), сила, ловкость, интеллект, опыт, уровень), оружие"""
        super().__init__(name, live, mana, power, knack, intel, exp, level)
        self.thisWeapon = weapon

    def scream(self):
        """Вывод сообщения о персонаже"""
        return f'Я герой {self.thisName} и я воин с {self.thisWeapon}'

    def attack(self, target, weapon, damage):
        """Метод атаки"""
        self.thisWeapon = weapon
        target.thisLive -= damage
        self.thisExp += 10
        if self.thisExp == 100:
            self.thisPower += 3
            self.thisKnack += 2
            self.thisIntel += 1
            self.thisExp = 0
        return f'{self.thisName} нанес {self.thisWeapon} {target.thisName} урон {damage}'
