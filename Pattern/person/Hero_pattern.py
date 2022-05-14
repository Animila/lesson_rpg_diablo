from rpg.Pattern.Character_pattern import Character
from rpg.Pattern.person.package import Package


class Hero(Character, Package):
    """Класс героя (наследует базового персонажа)"""

    def __init__(self, name, live, mana, power, knack, intel, exp, level, weapon='кулак'):
        """(Имя, здоровье, мана), сила, ловкость, интеллект, опыт, уровень"""
        super().__init__(name, live, mana)
        self.thisPower = power
        self.thisKnack = knack
        self.thisIntel = intel
        self.thisExp = exp
        self.thisLevel = level
        self.Pack = Package()
        self.Pack.thisPack['кулак'] = 10
        self.thisWeapon = [weapon, self.Pack.thisPack[weapon]]

    def scream(self):
        """Вывод сообщения героя"""
        return f'Я будущий герой {self.thisName}, но я выбрал специальность'

    def attack(self, target):
        """Метод атаки"""
        self.Pack.info()
        user_action = input('Выбор оружия:\n>').lower()
        weapon = self.thisWeapon[0]
        damage = self.thisWeapon[1]
        if user_action not in self.Pack.thisPack:
            self.thisWeapon = weapon
            target.thisLive -= damage
            self.thisExp += 10
            if self.thisExp == 100:
                self.thisPower += 3
                self.thisKnack += 2
                self.thisIntel += 1
                self.thisExp = 0
        else:
            self.thisWeapon = user_action
            target.thisLive -= self.Pack.thisPack[user_action]
            self.thisExp += 10
            if self.thisExp == 100:
                self.thisPower += 3
                self.thisKnack += 2
                self.thisIntel += 1
                self.thisExp = 0

        print(f'{self.thisName} нанес {weapon} {target.thisName} урон {damage}')
