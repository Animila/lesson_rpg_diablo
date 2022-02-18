from rpg.person.Hero_pattern import Hero

class Mag(Hero):
    '''Класс мага (наследует героя)'''

    def __init__(self, name, live, mana, power, knack, intel, exp, level):
        '''((Имя, здоровье, мана), сила, ловкость, интелект, опыт, уровень)'''
        super(Mag, self).__init__(name, live, mana, power, knack, intel, exp, level)
        self.thisSpells = []

    def scream(self):
        '''Вывод сообщения мага'''
        return f'Я маг герой {self.thisName} и я знаю {len(self.thisSpells)} заклинаний'

    def add_magic(self, magic):
        self.thisSpells.append(magic)
        self.thisExp += 10
        if self.thisExp == 100:
            self.thisPower += 1
            self.thisKhack += 2
            self.thisIntel += 4
            self.thisExp = 0
        print(f'{magic} добавлен в список заклинаний')