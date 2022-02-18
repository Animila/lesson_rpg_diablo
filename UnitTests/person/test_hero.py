import unittest
from rpg.person.Hero_pattern import Hero


class TestHero(unittest.TestCase):
    '''Тесты для класса Hero'''

    def test_scream(self):
        '''Проверка, на соотвествие значений'''

        # ввод данных
        test_result = 'Я будущий герой Миша, но я выбрал специальность'
        test_object = Hero('Миша', 34, 67, 89, 54, 56, 7, 2)
        test_status = test_object.scream()

        # проверка вывода строки
        self.assertEqual(test_status, test_result)

    def test_attack(self):
        '''Проверка атаки героя на цель'''

        # ввод данных
        test_result = 'Я будущий герой Миша, и я без оружия, но я нанес Денис урон 34 своими руками'
        test_object_1 = Hero('Миша', 100, 67, 89, 54, 56, 7, 2)
        test_object_2 = Hero('Денис', 100, 67, 89, 54, 56, 7, 2)

        # проверка вывода строки
        # проверка нанесения урона
        self.assertEqual(test_object_1.attack(test_object_2, 34), test_result)
        self.assertEqual(test_object_2.thisLive, 66)


if __name__ == '__name__':
    unittest.main()
