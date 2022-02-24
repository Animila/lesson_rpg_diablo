import unittest
from rpg.Pattern.Character_pattern import Character


class TestCharacter(unittest.TestCase):
    """Тесты для класса Character"""

    def test_drink_heal_potion(self):
        """Проверка, что можно ввести только целые числа"""

        # начальные данные
        this_Object = Character('misha', 23, 45)
        potion_1 = 2
        potion_2 = 'a'
        potion_3 = 9.4

        # применение данных
        potion_status_1 = this_Object.drink_heal_potion(potion_1)
        potion_status_2 = this_Object.drink_heal_potion(potion_2)
        potion_status_3 = this_Object.drink_heal_potion(potion_3)

        # Проверки:
        # 1. Если число целое - на положительное значение
        # 2. Если это не число - на соответствие 'Неверный тип значения'
        # 3. Если это не целое число - на соответствие 'Введено не целое число'
        self.assertTrue(potion_status_1)
        self.assertEqual(potion_status_2, 'Неверный тип значения')
        self.assertEqual(potion_status_3, 'Введено не целое число')


if __name__ == '__name__':
    unittest.main()
