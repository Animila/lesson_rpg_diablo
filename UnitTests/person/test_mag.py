import unittest
from rpg.Pattern.person.mag_pattern import Mag

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
        # 1. Есть ли в списке 'воздух'
        # 2. Есть ли в списке 'земля'
        # 3. На размер массив
        # 4. На соотвествие
        self.assertIn('воздух', test_object.thisSpells)
        self.assertIn('земля', test_object.thisSpells)
        self.assertTrue(len(test_object.thisSpells) == 2)
        self.assertEqual(test_status, test_result)

    def test_attach(self):
        '''Проверка на атаку'''

        # ввод данных
        test_result = 'Миша нанес воздух Никита урон 34'
        test_object_1 = Mag('Миша', 100, 0, 0, 0, 0, 0, 0)
        test_object_2 = Mag('Никита', 100, 0, 0, 0, 0, 0, 0)

        # эмуляция работы
        test_object_1.add_magic('воздух')
        test_status = test_object_1.attack(test_object_2, test_object_1.thisSpells[0], 34)

        # проверка
        # 1. На соотвествие
        # 2. На урон врагу
        self.assertEqual(test_status, test_result)
        self.assertEqual(test_object_2.thisLive, 66)

        test_object_3 = Mag('Миша', 100, 0, 0, 0, 0, 0, 0)
        test_object_4 = Mag('Никита', 100, 0, 0, 0, 0, 0, 0)

        print('3:',test_object_3.thisExp, test_object_3.thisPower, test_object_3.thisKhack, test_object_3.thisIntel)
        for i in range(10):
            test_object_3.attack(test_object_4, 'воздух', 34)
        print('4:',test_object_3.thisExp, test_object_3.thisPower, test_object_3.thisKhack, test_object_3.thisIntel)
        # проверка
        self.assertEqual(test_object_3.thisExp, 0)
        self.assertEqual(test_object_3.thisPower, 1)
        self.assertEqual(test_object_3.thisKhack, 2)
        self.assertEqual(test_object_3.thisIntel, 4)