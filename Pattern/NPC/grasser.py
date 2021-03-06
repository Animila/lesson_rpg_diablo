from rpg.Pattern.NPC.NPC_pattern import NPC


class Greaser(NPC):
    """Класс травника (наследует базового NPC)"""

    def __init__(self, name="Травник", live=100, mana=0, level=1):
        """(имя, здоровье, мана, уровень)"""
        super().__init__(name, live, mana, level)

    def scream(self):
        """вызов"""
        return f'Я {self.thisName}, обычный травник'

    def job(self, target, heal_potion):
        """Передает зелье ИГРОКУ"""
        heal_power = self.thisPack[heal_potion]
        target.thisLive += heal_power

    def make_potion(self, heal_potion, heal_power):
        """Добавляет зелье в вещи ТРАВНИКА"""
        # в переменную закидываем словарь из названия и силу
        # засовываем в словарь "словарь"
        up_potion = {heal_potion: heal_power}
        self.thisPack.update(up_potion)
