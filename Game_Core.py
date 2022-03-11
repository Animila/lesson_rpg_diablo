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

# словарь видов персонажей
person_list = {
    'маг': Mag,
    'воин': Warrior,
    'лучник': Archer,
}

# словарь видов NPC
NPC_list = {
    'кузнец': Craftsman(),
    'торговец': Trader(),
    'травник': Greaser(),
    'маг_путник': TravelMag()
}

# словарь демонов
devil_list = {
    'демон': Devil()
}

# виды оружия
armor = {
    'меч': 30,
    'топор': 20,
    'лук': 10,
}


# локация деревни
def village_ter(man):
    # цикл для общей деревни
    exit_village = False
    while not exit_village:
        print('Деревня')
        various_user = input('В деревне есть кузница, рынок. Куда вы направитесь?\n').lower()

        if various_user == 'кузница':
            print("Кузница")
            exit_user = False
            while not exit_user:
                print(' - Добрый день - поприветствовал вас кузнец, откладывая на стол молот - Вы что-то хотели?'
                      '\nВот что я могу сделать:')
                for element in armor:
                    print(f'\t- {element}')
                various_user = input('-> ').lower()
                NPC_list['кузнец'].job(man, various_user, armor[various_user])
                various_user = input('Что-то еще? (нет/да)\n').lower()
                if various_user == 'нет':
                    exit_user = True

        elif various_user == 'рынок':
            print('Рынок')
            exit_user = False
            while not exit_user:
                print(' - Ох, сколько лет, сколько зим - поприветствовал вас торговец, наблюдая за вами '
                      '- Вы что-то хотели?'
                      '\nВот что я могу сделать:')
                # various_user = input('-> ').lower()
                various_user = input('Что-то еще? (нет/да)\n').lower()
                if various_user == 'нет':
                    exit_user = True

        elif various_user == 'выход':
            print('Оглядываясь назад, вы еще раз прощаетесь с охранником на посту и покидаете деревню')
            exit_village = True

        else:
            print('Ошибка ввода. Повторите попытку')



def scale_ter(man):
    exit_scale = False
    while not exit_scale:
        print('Ущелье')
        print('Темное ущелье скрывает от вас многие тайны. Поэтому как только вы зашли внутрь, '
              'на вас выпрыгнуло какое-то существо')
        various_user = input("Убежать/Напасть?").lower()
        if various_user == "напасть":
            print("Затычка")
        if various_user == 'выход':
            exit_scale = True

# Начало игры
print(logo)
print('Добро пожаловать в нашу игру!')

# Ввод данных и выбор персонажа
user_name = input('Напишите свое имя: ')
user_var = input('Выберите класс (маг/воин/лучник): ').lower()

# Создание персонажа (имя)
user = person_list[user_var](user_name)

# Новая игры
print(new_game)
print(user.scream())
print('Открыв глаза вы только что осознали - перед вами новый мир. Неизвестный новый мир.\n'
      'Вы даже не знаете, как это произошло, потому что голова до сих пор нудит от боли.')
print('Вы осматриваетесь по сторонам и замечаете распутье и указатель.\n'
      'Справа находится небольшая деревня, слева - ущелье')
user_action = input('Куда же вы направитесь? ').lower()

if user_action == "направо" or user_action == 'деревня':
    village_ter(user)
elif user_action == 'налево' or user_action == 'ущелье':
    scale_ter(user)


print(user.Pack.thisPack)
