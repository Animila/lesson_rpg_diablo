from rpg.Pattern.person.Hero_pattern import Hero


class Archer(Hero):
    '''Класс Лучника (наследует героя)'''

    def __init__(self, name='лучник', live=100, mana=0, power=1, knack=5, intel=1, exp=0, level=1, weapon='лук'):
        '''((Имя, здоровье, мана), сила, ловкость, интелект, опыт, уровень)'''
        super().__init__(name, live, mana, power, knack, intel, exp, level)
        self.Pack.thisPack['лук'] = 20
        self.thisWeapon = {weapon, self.Pack.thisPack[weapon]}

    def scream(self):
        '''Вывод сообщения лучника'''
        return f'Я лучник герой {self.thisName}'