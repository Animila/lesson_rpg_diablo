from rpg.Pattern.person.Hero_pattern import Hero

class Archer(Hero):
    '''Класс Лучника (наследует героя)'''

    def __init__(self, name, live, mana, power, knack, intel, exp, level):
        '''((Имя, здоровье, мана), сила, ловкость, интелект, опыт, уровень)'''
        super(Archer, self).__init__(name, live, mana, power, knack, intel, exp, level)

    def scream(self):
        '''Вывод сообщения лучника'''
        return f'Я лучник герой {self.thisName}'

    def attack(self, target, damage):
        '''Атака лучника'''
        self.thisExp += 10
        if self.thisExp == 100:
            self.thisPower += 1
            self.thisKhack += 2
            self.thisIntel += 4
            self.thisExp = 0
        target.thisLive -= damage
        return f'{self.thisName} нанес {target.thisName} урон {damage}'
