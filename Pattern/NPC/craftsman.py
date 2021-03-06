from rpg.Pattern.NPC.NPC_pattern import NPC


class Craftsman(NPC):
    """Класс кузнеца (наследует базового NPC)"""

    def __init__(self, name="кузнец", live=100, mana=0, level=1):
        super().__init__(name, live, mana, level)

    def scream(self):
        """вызов"""
        return f'Я {self.thisName}, обычный Кузнец'

    def job(self, target, tool, damage):
        """Добавление в вещи игрока предмета"""
        weapon = {tool: damage}
        target.Pack.thisPack.update(weapon)
        print(f'Торговец сделал вам {tool} с уроном в {damage}')
