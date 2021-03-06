import unittest
from rpg.Pattern.Enemy.devil import Devil


class TestDevil(unittest.TestCase):
    """Тесты для класса Демона"""

    def test_steal_mana(self):
        """Проверка снятия маны"""
        test_object_1 = Devil('Misha', 0, 0, 0)
        test_object_2 = Devil('Nikita', 0, 100, 0)
        test_object_1.steal_mana(test_object_2, 30)

        self.assertEqual(test_object_2.thisMana, 70)


if __name__ == '__name__':
    unittest.main()