import unittest
from rpg.person.mag_pattern import Mag

class TestMag(unittest.TestCase):
    '''Тесты для класса Маг'''

    def test_UpState(self):
        '''Проверка повышения опыта и улучшение навыков'''
        # ввод данных
        test_object = Mag('Миша', 0, 0, 0, 0, 0, 0, 0)

        # эмуляция работы
        print(test_object.thisExp, test_object.thisPower, test_object.thisKhack, test_object.thisIntel)
        for i in range(10):
            test_object.add_magic('воздух')
        print(test_object.thisExp, test_object.thisPower, test_object.thisKhack, test_object.thisIntel)

        # проверка
        self.assertEqual(test_object.thisExp, 0)
        self.assertEqual(test_object.thisPower, 1)
        self.assertEqual(test_object.thisKhack, 2)
        self.assertEqual(test_object.thisIntel, 4)


    def test_magic_scream(self):
        '''Проверка на соотвествие'''

        # ввод данных
        test_result = 'Я маг герой Миша и я знаю 2 заклинаний'
        test_object = Mag('Миша', 0, 0, 0, 0, 0, 0, 0)
        test_object.add_magic('воздух')
        test_object.add_magic('земля')
        test_status = test_object.scream()

        # проверки
        # 1. Если в списке есть 'воздух'
        # 2. Соотвествие
        self.assertIn('воздух', test_object.thisSpells)
        self.assertIn('земля', test_object.thisSpells)
        self.assertEqual(test_status, test_result)

