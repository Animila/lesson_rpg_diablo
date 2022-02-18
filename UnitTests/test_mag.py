import unittest
from rpg.person.mag_pattern import Mag

class TestMag(unittest.TestCase):
    '''Тесты для класса Маг'''

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