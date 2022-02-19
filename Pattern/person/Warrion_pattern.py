from rpg.Pattern.person.Hero_pattern import Hero


class Warrion(Hero):
    '''Класс воина (наследует героя)'''

    def __init__(self, name, live, mana, power, knack, intel, exp, level, weapon):
        '''((Имя, здоровье, мана), сила, ловкость, интелект, опыт, уровень), оружие'''
        super(Warrion, self).__init__(name, live, mana, power, knack, intel, exp, level)
        self.thisWeapon = weapon

    def scream(self):
        '''вывод сообщения о персонаже'''
        return f'Я герой {self.thisName} и я воин с {self.thisWeapon}'

    def attack(self, target, damage):
        target.thisLive -= damage
        self.thisExp += 10
        if self.thisExp == 100:
                self.thisPower += 3
                self.thisKhack += 2
                self.thisIntel += 1
                self.thisExp = 0
        return f'{self.thisName} нанес {self.thisWeapon} {target.thisName} урон {damage}'

