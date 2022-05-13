from rpg.Pattern.person.Warrior import Warrior
from rpg.Pattern.NPC.craftsman import Craftsman
import unittest


class TestPackage(unittest.TestCase):
    """Тесты для класса вещей"""
        
    def test_add(self):
        war = Warrior()
        craft = Craftsman()
        craft.job(war, "mine", 100)
        war.Pack.info()

        self.assertIn("mine", war.Pack.thisPack)

    def test_uses(self):
        war_1 = Warrior(name="никита")
        war_2 = Warrior(name="Миша")
        craft = Craftsman()

        craft.job(war_1, "sword", 100)
        print(war_1.attack(war_2, "sword", war_1.Pack.thisPack["sword"]))

        self.assertEqual(war_2.thisLive, 0)


if __name__ == '__name__':
    unittest.main()

