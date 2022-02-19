from rpg.Pattern.Enemy.Enemy_pattern import Enemy


class Devil(Enemy):
    '''Класс черт (наследует противника)'''

    def __init__(self, name, live, mana, level):
        '''(Имя, здоровье, мана, уровень)'''
        super(Devil, self).__init__(name, live, mana, level)

    def steal_mana(self, target, damage):
        '''отбирает ману в '''
        target.thisMana -= damage