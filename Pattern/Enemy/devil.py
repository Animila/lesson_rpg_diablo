import random

from rpg.Pattern.Enemy.Enemy_pattern import Enemy


class Devil(Enemy):
    """Класс черт (наследует противника)"""

    def __init__(self, name='Демон', live=100, mana=0, level=1):
        """(Имя, здоровье, мана, уровень)"""
        super().__init__(name, live, mana, level)

    def steal_mana(self, target):
        """Отбирает ману у цели"""
        damage = random.randint(1, 30)
        target.thisLive -= damage
        print(f'Демон атаковал {target.thisName} на {damage}')
