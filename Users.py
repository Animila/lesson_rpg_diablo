from setting import Units
from art import logo


class UserController(Units):
    def __init__(self):
        super().__init__()

    def newUser(self):
        """Новая игры"""
        print(logo)
        print('Добро пожаловать в нашу игру!')

        # Ввод данных и выбор персонажа
        user_name = input('Напишите свое имя: ')
        user_var = input('Выберите класс (маг/воин/лучник) (по умолчанию - "воин"): ').lower()
        try:
            return self.hero[user_var]['создать'](name=user_name)
        except KeyError:
            print('ИСПОЛЬЗУЕТСЯ ГЕРОЙ ПО УМОЛЧАНИЮ')
            return self.hero['воин']['создать'](name=user_name)
        finally:
            print('Открыв глаза вы только что осознали - перед вами новый мир. Неизвестный новый мир.\n'
                  'Вы даже не знаете, как это произошло, потому что голова до сих пор нудит от боли.\n')