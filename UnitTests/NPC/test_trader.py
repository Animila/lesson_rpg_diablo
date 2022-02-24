from rpg.Pattern.NPC.trader import Trader
import unittest


class TestTrader(unittest.TestCase):
    """Тесты для класса торговца"""

    def test_scream(self):
        """Проверка вызова"""
        test_result = "Я Misha, обычный торговец"
        test_object = Trader("Misha", 100, 0, 0)
        test_status = test_object.scream()
        self.assertEqual(test_status, test_result)

    def test_job(self):
        test_object_1 = Trader("Misha", 100, 0, 0)
        test_object_2 = Trader("Nikita", 100, 0, 0)
        test_object_1.job(test_object_2, "sword", 100)

        # Проверка
        self.assertIn("sword", test_object_2.thisPack)

