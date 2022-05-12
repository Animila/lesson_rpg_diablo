from setting import *
from art import logo, new_game_logo


class Game:

    def newGame(self):
        """Новая игры"""

        # Ввод данных и выбор персонажа
        user_name = input('Напишите свое имя: ')
        user_var = input('Выберите класс (маг/воин/лучник) (по умолчанию - "воин"): ').lower()
        try:
            return units[0][user_var]['создать'](name=user_name)
        except KeyError:
            print('ИСПОЛЬЗУЕТСЯ ГЕРОЙ ПО УМОЛЧАНИЮ')
            return units[0]['воин']['создать'](name=user_name)
        finally:
            print('Открыв глаза вы только что осознали - перед вами новый мир. Неизвестный новый мир.\n'
                  'Вы даже не знаете, как это произошло, потому что голова до сих пор нудит от боли.\n')


print(logo)
print('Добро пожаловать в нашу игру!')
game = Game()
user = game.newGame()
user.Status()
