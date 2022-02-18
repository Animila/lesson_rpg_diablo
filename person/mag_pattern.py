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
        print(f'{magic} добавлен в список заклинаний')