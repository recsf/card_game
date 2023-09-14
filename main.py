import sys


def play(argv):
    deck = Deck()
    hands = []
    for i in range(1, 5):
        player = 'Player %d' % i
        if len(argv) > i:
            player = argv[i]
        hands.append(Hand(player))

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())
    print(hands[0])
    input("Lets start playing. Press any key to continue: ")

    for i in range(1, 14):
        cards = []
        floors = []
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)
            floors.append(hand.getlabel() + " : " + str(card))
        winner_card = deck.wincard(cards)
        winner_hand = hands[cards.index(winner_card)]
        winner_hand.roundwinner()
        print("Round", i, ":-", ",".join(floors), ", Winner :- ", winner_hand.getlabel(), ":", winner_card)
    for hand in hands:
        print("Score for", hand.getlabel(), "is", hand.getwincount())


def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Play Again(Y/N)?: ")
    print("Bye bye")


if __name__ == '__main__':
    main(sys.argv)
