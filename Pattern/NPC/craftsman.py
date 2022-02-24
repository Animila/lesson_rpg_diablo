from rpg.Pattern.NPC.NPC_pattern import NPC


class Craftsman(NPC):
    """Класс кузнеца (наследует базового NPC)"""

    def __init__(self, name, live, mana, level):
        super().__init__(name, live, mana, level)

    def scream(self):
        """вызов"""
        return f'Я {self.thisName}, обычный Кузнец'

    def job(self, target, tool, state):
        """Добавление в вещи игрока предмета"""
        weapon = {tool: state}
        target.thisPack.update(weapon)
