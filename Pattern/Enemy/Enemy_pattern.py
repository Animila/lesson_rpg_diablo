from rpg.Pattern.Character_pattern import Character


class Enemy(Character):
    """Класс противника (наследует базового персонажа)"""

    def __init__(self, name, live, mana, level):
        """(Имя, здоровье, мана), уровень"""
        super().__init__(name, live, mana)
        self.thisLevel = level
        self.thisObject = []

    def attack(self, target):
        """Атака противника на цель (на вход принимается цель)"""
        return f'{self.thisName} атаковал {target.thisName}'

