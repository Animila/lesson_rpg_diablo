import unittest
from rpg.Pattern.person.Warrior import Warrior


class TestWarrior(unittest.TestCase):
    """Тесты для класса Воина"""

    def test_UpState(self):
        """Проверка повышения опыта и улучшения"""

        # ввод данных
        test_object_1 = Warrior('Миша', 100, 0, 1, 1, 1, 0, 1, 'нож')
        test_object_2 = Warrior('Денис', 100, 67, 89, 54, 56, 7, 2, 'мяч')

        # Эмуляция работы
        # 1. Выводится первоначальные значения
        # 2. Производится атака до 100 опыта
        # 3. Выводится итоговые значения после работы
        print(test_object_1.thisExp, test_object_1.thisPower, test_object_1.thisKhack, test_object_1.thisIntel)
        for i in range(10):
            test_object_1.attack(test_object_2, 33)
        print(test_object_1.thisExp, test_object_1.thisPower, test_object_1.thisKhack, test_object_1.thisIntel)

        # Проверка данных
        self.assertEqual(test_object_1.thisPower, 4)
        self.assertEqual(test_object_1.thisKhack, 3)
        self.assertEqual(test_object_1.thisIntel, 2)
        self.assertEqual(test_object_1.thisExp, 0)

    def test_scream(self):
        """Проверка, на соотвествие значений"""

        # ввод данных
        test_result = 'Я герой Миша и я воин с нож'
        test_object = Warrior('Миша', 100, 67, 89, 54, 56, 7, 2, 'нож')
        test_status = test_object.scream()

        # проверка на соответствие
        self.assertEqual(test_status, test_result)

    def test_attach(self):
        """Проверка на атаку воина"""

        # ввод данных
        test_result = 'Миша нанес нож Денис урон 33'
        test_object_1 = Warrior('Миша', 34, 67, 89, 54, 56, 7, 2, 'нож')
        test_object_2 = Warrior('Денис', 100, 67, 89, 54, 56, 7, 2, 'мяч')
        test_status = test_object_1.attack(test_object_2, 33)
        print(test_status)

        # проверка вывода строки
        # проверка нанесения урона
        self.assertEqual(test_status, test_result)
        self.assertEqual(test_object_2.thisLive, 67)


if __name__ == '__name__':
    unittest.main()
