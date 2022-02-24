from rpg.Pattern.NPC.NPC_pattern import NPC


class TravelMag(NPC):
    """Класс странствующего мага (наследует базовый НПС)"""

    def __init__(self, name, live, mana, level):
        super().__init__(name, live, mana, level)

    def scream(self):
        """вызов"""
        return f'Я {self.thisName}, странствующий торговец'

    def job(self, target, product, state):
        """Добавление в вещи игрока предмета"""
        trade_force = {product: state}
        target.thisPack.update(trade_force)
