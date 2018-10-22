cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 5]
def game():
    dealer1 = cards.pop()
    dealer2 = cards.pop()
    print('Dealer:', dealer1, dealer2)
    gamer1 = cards.pop()
    gamer2 = cards.pop()
    gamerscore = gamer1 + gamer2
    print('Gamer: ', gamer1, gamer2)
    while True:
        zapros = input('Еще карту ?')
        if zapros == 'y':

game()















