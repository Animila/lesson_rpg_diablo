from Pattern.person.archer import Archer
from Pattern.person.mag import Mag
from Pattern.person.Warrior import Warrior
from art import logo, new_game
import os

# словарь видов персонажей
person = {
    'маг': Mag,
    'лучник': Archer,
    'воин': Warrior
}


class Game:
    """Класс запуска игры"""

    def __init__(self):
        """Выполнение цели, старт"""
        self.target = False
        self.user = ''
        self.start()

    def start(self):
        """Старт игры"""
        print(logo)
        print('Добро пожаловать в нашу игру!')
        user_name = input('Напишите свое имя: ')
        user_var = input('Выберите класс (маг/воин/лучник): ').lower()

        self.user = person[user_var](name=user_name)
        self.games()

    def games(self):
        """Метод самой игры"""
        os.system('\n\n\n\n\n\n\n')
        print(new_game)
        user_var = input('Ваши действия? \n')


objects = Game()
