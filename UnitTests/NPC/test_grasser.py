import unittest
from rpg.Pattern.NPC.grasser_pattern import Greaser


class TestGreaser(unittest.TestCase):
    """Тесты для класса травника"""

    def test_scream(self):
        """Тест вызова"""
        # ввод данных
        test_result = 'Я Миша, обычный травник'
        test_object = Greaser('Миша', 100, 0, 0)
        test_status = test_object.scream()

        # Проверка на соответствие значений
        self.assertEqual(test_status, test_result)

    def test_make(self):
        """Тест создания зелья"""
        # Ввод данных
        test_object = Greaser('Миша', 100, 0, 0)
        test_object.make_potion('Grass', 0)
        test_object.make_potion('Snake', 973)

        # Проверка на соответствие значений
        # 1-2 - значения
        # 3 - на длину словаря
        self.assertEqual(test_object.thisPack["Grass"], 0)
        self.assertEqual(test_object.thisPack["Snake"], 973)
        self.assertEqual(len(test_object.thisPack), 2)

    def test_job(self):
        """Проверка работы с применением зелья"""

        # Ввод данных
        test_object_1 = Greaser('Миша', 100, 0, 0)
        test_object_2 = Greaser('Никита', 1, 0, 0)

        # имитация работы
        test_object_1.make_potion('Snake', 3)
        test_object_1.job(test_object_2, "Snake")

        # Проверка на соответствие
        self.assertEqual(test_object_2.thisLive, 4)


if __name__ == '__name__':
    unittest.main()
