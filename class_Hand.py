import class_Deck


class Hand:
    def __init__(self, label=""):
        self.cards = []
        self.label = label
        self.wincount = 0

    def getlabel(self):
        return self.label

    def roundwinner(self):
        self.wincount += 1

    def getwincount(self):
        return self.wincount

    def __str__(self):
        return "Card for " + self.label + " is " + class_Deck.Deck.__str__(self)
