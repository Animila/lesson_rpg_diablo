from Pattern.person.archer_pattern import Archer
from Pattern.person.mag_pattern import Mag
from Pattern.person.Warrion_pattern import Warrion
from art import logo, new_game
import os

#словарь видов персонажей
person = {
    'маг': Mag,
    'лучник': Archer,
    'воин': Warrion
}

class Game:
    def __init__(self):
        self.target = False
        self.start()

    def start(self):
        print(logo)
        print('Добро пожаловать в нашу игру!')
        user_name = input('Напиишите свое имя: ')
        user_var = input('Выберите класс (маг/воин/лучник): ').lower()

        self.user = person[user_var](name=user_name)
        self.games()

    def games(self):
        os.system('\n\n\n\n\n\n\n')
        print(new_game)

object = Game()

