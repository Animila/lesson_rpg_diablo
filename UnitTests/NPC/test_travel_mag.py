from rpg.Pattern.NPC.travel_mag import TravelMag
import unittest


class TestTravelMag(unittest.TestCase):
    """Тесты для класса торговца"""

    def test_scream(self):
        """Проверка вызова"""
        test_result = "Я Misha, странствующий торговец"
        test_object = TravelMag("Misha", 100, 0, 0)
        test_status = test_object.scream()
        self.assertEqual(test_status, test_result)

    def test_job(self):
        test_object_1 = TravelMag("Misha", 100, 0, 0)
        test_object_2 = TravelMag("Nikita", 100, 0, 0)
        test_object_1.job(test_object_2, "sword", 100)

        # Проверка
        self.assertIn("sword", test_object_2.thisPack)

