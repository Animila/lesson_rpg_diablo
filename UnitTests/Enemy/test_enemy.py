import unittest
from rpg.Pattern.Enemy.Enemy_pattern import Enemy


class TestEnemy(unittest.TestCase):
    """Тесты для класса базового врага"""

    def test_attack(self):
        """Проверка атаки"""
        # ввод данных
        test_result = 'Миша атаковал Никита'
        test_object_1 = Enemy('Миша', 100, 0, 0)
        test_object_2 = Enemy('Никита', 100, 0, 0)
        test_status = test_object_1.attack(test_object_2)

        # проверка
        self.assertEqual(test_status, test_result)


if __name__ == '__name__':
    unittest.main()