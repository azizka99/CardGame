cards = [2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 2, 5]
def game():
    dealer1 = cards.pop()
    dealer2 = cards.pop()
    dealerscore = dealer1 + dealer2
    print('Dealer:', dealer1, dealer2)
    gamer1 = cards.pop()
    gamer2 = cards.pop()
    gamerscore = gamer1 + gamer2
    print('Gamer: ', gamer1, gamer2)
    while True:
        zapros = input('Еще карту ? ')
        if zapros == 'y':
            gamer1 = cards.pop()
            gamerscore += gamer1
            print(gamer1, gamerscore)
            if gamerscore > 21:
                print('Вы проиграли :(')
                break
            elif gamerscore == 21:
                break
        if zapros == 'n':
            break
    while dealerscore <= 17:
        dealer1 = cards.pop()
        dealerscore += dealer1
        print(dealer1, dealerscore)
    if dealerscore > 21:
        print('Вы выиграли!')
    elif dealerscore > gamerscore:
        print('Выиграл Диллер!')
    elif  dealerscore < gamerscore:
        print('Вы выиграли')



game()















