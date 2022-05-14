from random import randint

from Users import UserController
from listsPlace import Places


class Game(UserController, Places):
    def __init__(self):
        super().__init__()
        self.hero = self.newUser()
        self.listAction = {
            'статус': self.hero.Status,
            'мешок': self.hero.Pack.info,
            'восстановить ману': self.hero.drink_mana_potion,
            'восстановить здоровье': self.hero.drink_heal_potion,
            'выход': None,
            'локации': self.locations,
        }
        self.views()

    def views(self):
        while True:
            print('Список действий: ')
            for i in self.listAction:
                print(f'- {i}')
            user_var = input('Ваши действия:\n>').lower()
            if user_var == 'выход':
                return
            if user_var == 'восстановить ману' or user_var == 'восстановить здоровье':
                self.listAction[user_var](randint(5, 20))
            elif user_var == 'локации':
                self.listAction[user_var](self.hero)
            elif user_var not in self.listAction:
                print('Ошибка ввода')
            else:
                self.listAction[user_var]()

game = Game()
