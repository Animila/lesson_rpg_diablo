from rpg.Character_pattern import Character


class NPC(Character):
    '''Класс базового НПС'''

    def __init__(self, name, live, mana, level):
        '''(имя, здоровье, мана), уровень'''
        super(NPC, self).__init__(name, live, mana)
        self.thisLevel = level
        self.thisPack = []

    def scream(self):
        return f'Я {self.thisName}, обычный NPC!'
