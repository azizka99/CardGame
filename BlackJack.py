import  random
def clear():
    clear = "\n" * 10
    print(clear)

cards = []

def koloda():
    a = 0
    b = 0
    bottomCard = 2
    f = 0
    mastNum = 4
    while a < 10:
        for i in range(mastNum):
            cards.append(bottomCard)
        a += 1
        bottomCard += 1
    while f < 3:
        for i in range(4):
            cards.append(10)
        f += 1
def iqra():
    a = random.choice(cards)
    cards.remove(a)
    b = random.choice(cards)
    cards.remove(b)
    nick1score = a + b
    print(a, b)

koloda()
a = 0
nickname1 = input()
nickname2 = input()
while a < 26:
    iqra()
    a += 1













