import random
from collections import deque

cards = deque()
clear_deck = []


def create_deck():
    bottomCard = 2
    a = bottomCard
    suitNum = 4
    while a <= 14:
        for i in range(suitNum):
            clear_deck.append(a)
        a += 1


def shuffle_deck():
    return random.sample(clear_deck, len(clear_deck))


create_deck()
cards += shuffle_deck()


# ============================================================
def real_num(current_card):
    if current_card >= 12:
        return 10
    # elif current_card == 11:

    else:
        return current_card


def printed_card(real_card):
    if real_card == 12:
        return 'Jack'
    elif real_card == 13:
        return 'Queen'
    elif real_card == 14:
        return 'King'
    elif real_card == 11:
        return 'Ace'
    else:
        return real_card


# ============================================================
def game():
    dealer_hand = deque()
    gamer_hand = deque()
    lost = 0
    dealer_hand.append(cards.popleft())
    dealer_hand.append(cards.popleft())
    dealerscore = real_num(dealer_hand[0]) + real_num(dealer_hand[1])
    print('Dealer:', printed_card(dealer_hand[0]), printed_card(dealer_hand[1]))
    gamer1 = cards.popleft()
    gamer2 = cards.popleft()
    gamerscore = real_num(gamer1) + real_num(gamer2)
    print('Gamer: ', printed_card(gamer1), printed_card(gamer2))
    while True:
        if gamerscore == 21:
            break
        zapros = input('Еще карту ? ')
        if zapros == 'y' or zapros == '1':
            gamer1 = cards.popleft()
            gamerscore += real_num(gamer1)
            print(printed_card(gamer1), '|||', 'Ваш счет:', gamerscore)
            if gamerscore > 21:
                print('Вы проиграли :(')
                lost = 1
                break
            elif gamerscore == 21:
                break
        if zapros == 'n' or zapros == '2':
            break
    if lost == 1:
        return
    while dealerscore < 17:
        dealer1 = cards.popleft()
        dealerscore += real_num(dealer1)
        print('Dealer: ', printed_card(dealer1), '|||', 'Счет диллера:', dealerscore)
    if dealerscore > 21:
        print('Вы выиграли!')
    elif dealerscore > gamerscore:
        print('Выиграл Диллер!')
    elif dealerscore < gamerscore:
        print('Вы выиграли')
    elif dealerscore == gamerscore:
        print('Push')


while True:
    game()
    ks = input('Продолжать игру 1/2')
    if ks == '2' or ks == 'n':
        break














