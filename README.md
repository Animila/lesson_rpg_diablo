# Игра Diablo
## (в формате текстового рпг)

### !!!ВНИМАНИЕ!!!
>_Данный репозиторий был создан в качестве демонстрации навыков работы в Python и GitHub._
>
>Автор кода: Христофоров Илья


Короче, Кодер, я на гит запущил и в благородство играть не буду: проверишь код и поставишь оценку — и мы в расчете. Заодно посмотрим, как быстро твой компьютер сможет перелопатить весь этот код. Фиг его знает, зачем я столько Unit тестов зафигачил, но если захочешь что-то изменить - открывай новую ветку или форкай на свой репозиторий. Если захочешь поковырять в класса персонажей или, не дай бог, в Character_pattern - то одевай перчатки и не забывай запускать юнит тесты. Для таких именно случаев и делал, а не по приколу. 

А что по поводу зависимостей и наследования - то папочка тут это character_pattern, его дети - NPC_pattern, Hero_pattern, Enemy_pattern. И уже от них можешь создавать новых юнитов. И да, все дети инициировали свои поля, так что в игре надо только ввести имя. Запомни:

>ЗНАЧЕНИЯ ПОЛЕЙ КОНСТРУКТОРА НАДО ИНИЦИИРОВАТЬ ТОЛЬКО В ДЕТЯХ ВСЕХ БАЗОВЫХ КЛАССОВ

## Character_pattern

Это отец всех отцов, можно даже сказать основатель.
В полях у него находится имя для персонаж, количество жизней и маны

Метод Status - выводит текущие значения вышеукзанных полей в красивом виде. 
Метод drink_heal_potion -
Метод drink_mana_potion -

## Hero
Наследует базового персонажа
