from rpg.Pattern.Character_pattern import Character


class Hero(Character):
    """Класс героя (наследует базового персонажа)"""

    def __init__(self, name, live, mana, power, knack, intel, exp, level):
        """(Имя, здоровье, мана), сила, ловкость, интелект, опыт, уровень"""
        super().__init__(name, live, mana)
        self.thisPower = power
        self.thisKnack = knack
        self.thisIntel = intel
        self.thisExp = exp
        self.thisLevel = level

    def scream(self):
        """Вывод сообщения героя"""
        return f'Я будущий герой {self.thisName}, но я выбрал специальность'

    def attack(self, target, damage):
        """Атака героя на цель (на вход принимается цель и сила урона)"""
        target.thisLive -= damage
        return f'Я будущий герой {self.thisName}, и я без оружия, ' \
               f'но я нанес {target.thisName} урон {damage} своими руками'
