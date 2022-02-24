from rpg.Pattern.Enemy.Enemy_pattern import Enemy


class Devil(Enemy):
    """Класс черт (наследует противника)"""

    def __init__(self, name, live, mana, level):
        """(Имя, здоровье, мана, уровень)"""
        super().__init__(name, live, mana, level)

    def steal_mana(self, target, damage):
        """Отбирает ману у цели"""
        target.thisMana -= damage
