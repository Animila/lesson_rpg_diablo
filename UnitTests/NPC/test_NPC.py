import unittest
from rpg.Pattern.NPC.NPC_pattern import NPC


class TestNPC(unittest.TestCase):
    """Тесты для базового класса NPC"""

    def test_scream(self):
        """Проверка на вызов"""
        # ввод данных
        test_result = 'Я Миша, обычный NPC!'
        test_object = NPC('Миша', 0, 0, 0)
        test_status = test_object.scream()

        # Проверка
        self.assertEqual(test_status, test_result)


if __name__ == '__name__':
    unittest.main()