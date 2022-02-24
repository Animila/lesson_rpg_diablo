import unittest
from rpg.Pattern.person.archer import Archer


class TestArcher(unittest.TestCase):
    """Тесты для класса лучника"""

    def test_scream(self):
        """Проверка вывода"""
        # ввод данных
        test_result = 'Я лучник герой Миша'
        test_object = Archer('Миша', 0, 0, 0, 0, 0, 0, 0)
        test_status = test_object.scream()

        # проверка
        self.assertEqual(test_status, test_result)

    def test_attach(self):
        """Тест атаки"""
        # ввод данных
        test_object_1 = Archer('Миша', 100, 0, 0, 0, 0, 0, 0)
        test_object_2 = Archer('Никита', 100, 0, 0, 0, 0, 0, 0)

        # эмуляция работы
        print('3:', test_object_1.thisExp, test_object_1.thisPower, test_object_1.thisKhack, test_object_1.thisIntel)
        for i in range(10):
            test_object_1.attack(test_object_2, 34)
        print('4:', test_object_1.thisExp, test_object_1.thisPower, test_object_1.thisKhack, test_object_1.thisIntel)

        # проверка
        self.assertEqual(test_object_1.thisExp, 0)
        self.assertEqual(test_object_1.thisPower, 1)
        self.assertEqual(test_object_1.thisKhack, 2)
        self.assertEqual(test_object_1.thisIntel, 4)


if __name__ == '__name__':
    unittest.main()
