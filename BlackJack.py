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
#============================================================
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


def score(hand):
    current_score = 0
    ace = 0
    for i in hand:
        if i == 11:
            current_score += 1
            ace = 1
        elif i >= 12:
            current_score += 10
        else:
            current_score += i
    if current_score <= 11 and ace == 1:
        current_score += 10
    return current_score

def show(hand):
    for i in hand:
        print(printed_card(i), end = ' ')
    print()


#============================================================
def game():

    dealer_hand = deque()
    gamer_hand = deque()
    lost = 0
    dealer_hand.append(cards.popleft())
    dealer_hand.append(cards.popleft())
    dealerscore = score(dealer_hand)
    print('Dealer: ', end = '')
    show(dealer_hand)
    gamer_hand.append(cards.popleft())
    gamer_hand.append(cards.popleft())
    gamerscore = score(gamer_hand)
    print('Gamer: ', end = '')
    show(gamer_hand)
    while True:
        if gamerscore == 21:
            break
        zapros = input('Еще карту ? ')
        if zapros == 'y' or zapros == '1':
            gamer_hand.append(cards.popleft())
            gamerscore = score(gamer_hand)
            print('Gamer: ', end = '')
            show(gamer_hand)
            print('Ваш счет:', gamerscore)
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
        dealer_hand.append(cards.popleft())
        dealerscore = score(dealer_hand)
        print('Dealer: ', end= '')
        show(dealer_hand)
        print('Счет диллера:', dealerscore)
    if dealerscore > 21:
        print('Вы выиграли!')
    elif dealerscore > gamerscore:
        print('Выиграл Диллер!')
    elif  dealerscore < gamerscore:
        print('Вы выиграли')
    elif dealerscore == gamerscore:
        print('Push')


while True:
    game()
    ks = input('Продолжать игру 1/2')
    if ks == '2' or ks == 'n':
        break














