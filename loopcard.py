import random
cards = []


def create_deck():
    bottomCard = 2
    a = bottomCard
    suitNum = 4
    while a <= 14:
        for i in range(suitNum):
            cards.append(a)
        a += 1


def shuffle_deck(deck):
    return random.sample(deck, len(deck))


create_deck()
print(shuffle_deck(cards))