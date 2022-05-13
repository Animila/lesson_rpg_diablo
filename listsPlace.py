import random

from rpg.setting import Units


class Village:
    def __init__(self, user):
        self.user = user
        print('---Деревня---')
        self.armor = {
            'меч': 30,
            'топор': 40,
            'лук': 70,
            'булава': 1,
        }
        self.goods = {
            'яблоко': 12,
            'зелье здоровья': 23,
            'ядерное оружие': 99999999999999,
        }
        self.select()

    def select(self):
        user_action = input('В деревне есть кузница, рынок. Куда вы направитесь? ("Выход" - вернуться в меню)\n>').lower()
        list_place = {
            'кузница': self.forge,
            'рынок': self.market,
        }
        if user_action == 'выход':
            Places().locations(self.user)
        list_place[user_action]()

    def forge(self):
        print("----Кузница----")
        print(' - Добрый день - поприветствовал вас кузнец, откладывая на стол молот')

        while input(' - Что-то хотите? (нет/да)\n').lower() == 'да':
            print('Вот что я могу сделать:')
            for element in self.armor.items():
                print(f'\t- {element[0]}: {element[1]}')
            user_action = input('-> ').lower()
            trader = Units().npc['кузнец']['создать']
            trader.job(self, target=self.user, tool=user_action, damage=int(self.armor[user_action]))
            print('Спасибо за приобретение')

    def market(self):
        print('Рынок')
        exit_user = False
        while not exit_user:
            print(' - Ох, сколько лет, сколько зим - поприветствовал вас торговец, наблюдая за вами '
                  '- Вы что-то хотели?'
                  '\nВот что я могу предложить:')
            for i in self.goods:
                print(f'- {i}')
            user_action = input('Уже решили, что взять?\n>').lower()
            trader = Units().npc['торговец']['создать']
            if user_action == 'ядерное оружие':
                print('ХРЕН ТЕБЕ А НЕ ЧИТЫ ')
            else:
                trader.job(self, target=self.user, product=user_action, state=int(self.goods[user_action]))
            print('Спасибо за приобретение')
            user_action = input('Что-то еще? (нет/да)\n').lower()
            if user_action == 'нет':
                exit_user = True


class Scale:
    def __init__(self, user):
        self.user = user
        self.action_list = {
            'атака': self.user.attack,
            'восстановить здоровье': self.user.drink_heal_potion,
            'восстановить ману': self.user.drink_mana_potion,
            'статус': self.user.Status,
            'выход': None
        }
        self.war()

    def war(self):
        devil = Units().devil['демон']['создать']()
        print('Неожиданно перед вами появился демон. Начинается бой')
        while True:
            self.user.Status()
            devil.Status()
            for i in self.action_list:
                print(f'- {i}')
            user_action = input('Ваши действия:\n>').lower()
            if user_action == 'выход':
                return
            if user_action in self.action_list:
                if user_action == 'атака':
                    self.action_list[user_action](devil)
                    devil.steal_mana(self.user)
                elif user_action == 'восстановить здоровье':
                    self.action_list[user_action](random.randint(1, 30))
                else:
                    self.action_list[user_action]()
            if devil.thisLive <= 0:
                print('По итогу сражения демон был повержен, а вы получили опыт')
                Places().locations(self.user)


    # def POSHEL(self):
    #     exit_scale = False
    #     while not exit_scale:
    #         print('Ущелье')
    #         print('Темное ущелье скрывает от вас многие тайны. Поэтому как только вы зашли внутрь, '
    #               'на вас выпрыгнуло какое-то существо')
    #         various_user = input("Убежать/Напасть?").lower()
    #         if various_user == "напасть":
    #             print("Затычка")
    #         if various_user == 'выход':
    #             exit_scale = True


class Places(Village, Scale):
    def __init__(self):
        super().__init__(self)

    def locations(self, user):
        places = {
            'деревня': Village,
            'ущелье': Scale,
            'выход': None
        }
        print('Куда можно попасть: ')
        for place in places:
            print(f' - ' + place)
        user_var = input('>').lower()
        places[user_var](user)
