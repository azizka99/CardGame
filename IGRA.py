def clear():
    clear = "\n" * 10
    print(clear)


cards = []
a = 0
b = 0
c = 2
f = 0
uqadka = 0
while  a < 10:
    for i in range(4):
        cards.append(c)
    a += 1
    c += 1
while f < 3:
    for i in range(4):
        cards.append(10)
    f += 1
while True:
    number = int(input('Номер карты: '))
    print('================================================')
    if number > 11:
        k = input()
        if k == 'exit':
            break
    else:
        if number == 0 or number == 1:
            number1 = int(input())
            number = number1
        cards.remove(number)
        print('Сколько таких карт осталось: ', cards.count(number))
        print('------------------------------------------------------------')
        print(cards)
        print('------------------------------------------------------------')
        print('Сколько вообщем карт осталось: ', len(cards))
        print('============================================================')
        if number == 2 or number == 3 or number == 4 or number == 5 or number == 6:
            uqadka += 1
        elif number == 10 or number == 11:
            uqadka -= 1
        print('plyus minus =', uqadka)
        print('============================================================')
        clear()
