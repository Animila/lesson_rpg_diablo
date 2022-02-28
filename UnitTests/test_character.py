import unittest
from rpg.Pattern.Character_pattern import Character


class TestCharacter(unittest.TestCase):
    """Тесты для класса Character"""

    def test_drink_heal_potion(self):
        """Проверка, что можно ввести только целые числа"""
        test_object = Character("Misha", 100, 0)
        test_object.drink_heal_potion(10)
        self.assertEqual(test_object.thisLive, 110)

    def test_drink_mana_potion(self):
        test_object = Character("Misha", 100, 0)
        test_object.drink_mana_potion(10)
        self.assertEqual(test_object.thisMana, 10)


if __name__ == '__name__':
    unittest.main()
