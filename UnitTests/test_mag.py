import unittest
from rpg.person.mag_pattern import Mag

class TestMag(unittest.TestCase):
    '''Тесты для класса Маг'''

    def test_scream(self):
        '''Проверка на соотвествие'''

        # ввод данных
        test_result = 'Я маг герой Миша и я знаю 1 заклинаний'
        test_object = Mag('Миша', 0, 0, 0, 0, 0, 0, 0)
        test_object.thisSpells.append('i')
        test_status = test_object.scream()

        # проверка
        self.assertEqual(test_status, test_result)