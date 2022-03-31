# Импорт героев
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

# прочие импорты
from art import logo, new_game

# Словарь персонажей
# 1.главные персонажи
# 2.второстепенные персонажи
# 3. враги
units = [
    {
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
    },
    {
        'кузнец':
            {
                'создать': Craftsman,
                'крик': Craftsman.scream,
                'работа': Craftsman.job,
             },
        'торговец':
            {
                'создать': Trader,
                'атака': Mag.attack
            },
        'травник':
            {
                'создать': Greaser,
                'атака': Archer.attack
            },
        'маг_путник':
            {
                'создать': TravelMag,
                'атака': Archer.attack
            },
    },
    {
        'демон':
            {
                'создать': Devil,
                'атака': Warrior.attack
            },
    }
]


def start_game():
    print(logo)
    print('Добро пожаловать в нашу игру!')
    user = create_user()
    print(new_game)
    print(user.scream())
    print('Открыв глаза вы только что осознали - перед вами новый мир. Неизвестный новый мир.\n'
          'Вы даже не знаете, как это произошло, потому что голова до сих пор нудит от боли.')
    print('Вы осматриваетесь по сторонам и замечаете распутье и указатель.\n'
          'Справа находится небольшая деревня, слева - ущелье')
    user_action = input('Куда же вы направитесь? ').lower()

    # place(user_action)

def create_user():
    # Ввод данных и выбор персонажа
    user_name = input('Напишите свое имя: ')
    user_var = input('Выберите класс (маг/воин/лучник): ').lower()
    try:
        return units[0][user_var]['создать'](name=user_name)
    except KeyError:
        print('Ошибка выбора персонажа')

start_game()




