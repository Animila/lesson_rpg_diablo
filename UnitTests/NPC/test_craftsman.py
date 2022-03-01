from rpg.Pattern.NPC.craftsman import Craftsman
from rpg.Pattern.person.Warrior import Warrior
import unittest


class TestCraftsmen(unittest.TestCase):
    """Тесты для класса кузнеца"""

    def test_scream(self):
        """Проверка вывода"""

        # Ввод данных
        test_result = "Я Misha, обычный Кузнец"
        test_object = Craftsman("Misha", 100, 0, 0)
        test_status = test_object.scream()

        # Проверка
        self.assertEqual(test_status, test_result)

    def test_job(self):
        """Проверка добавления предмета в инвентарь"""
        # ввод данных
        test_object_1 = Craftsman("Misha", 100, 0, 0)
        test_object_2 = Warrior()
        test_object_1.job(test_object_2, "sword", 100)

        # Проверка
        self.assertIn("sword", test_object_2.Pack.thisPack)
