from Pattern.person.archer import Archer
from Pattern.person.mag import Mag
from Pattern.person.Warrior import Warrior

# импорт NPC
from Pattern.NPC.craftsman import Craftsman
from Pattern.NPC.trader import Trader
from Pattern.NPC.grasser import Greaser
from Pattern.NPC.travel_mag import TravelMag

# импорт злодеев
from Pattern.Enemy.devil import Devil


class Units(Devil, Warrior, Archer, Mag, Trader, Craftsman, Greaser, TravelMag):

    def __init__(self):
        super().__init__()
        self.hero = {
            'воин':
                {
                    'создать': Warrior,
                    'атака': Warrior.attack,
                    'крик': Warrior.scream,
                },
            'маг':
                {
                    'создать': Mag,
                    'крафт': Mag.add_magic,
                    'атака': Mag.attack,
                    'крик': Warrior.scream,
                },
            'лучник':
                {
                    'создать': Archer,
                    'атака': Archer.attack,
                },
        }
        self.devil = {
            'демон':
                {
                    'создать': Devil,
                    'атака': Devil().steal_mana,
                    'статус': Devil().Status
                },
        }
        self.npc = {
           'кузнец':
               {
                   'создать': Craftsman,
                   'крик': Craftsman.scream,
                   'работа': Craftsman.job,
               },
           'торговец':
               {
                   'создать': Trader,
                   'работа': Trader.job,
               },
           'травник':
               {
                   'создать': Greaser,
                   'работа': Greaser.job,
               },
           'маг_путник':
               {
                   'создать': TravelMag,
                   'работа': TravelMag.job,
               },
       }
