from Globals import UTILITIES
class CardGroup:
    def __init__(self,cards):
        CardGroup.setCards(self,cards)
    def setCards(self,cards):
        self.cards=cards
        self.playedcards=[]
        self.sort()
    def findCard(self,card):
        for i in range(len(self.cards)):
            if card==self.cards[i]:
                return i
        return None
    def getCardIndex(self,card):
        for ii in range(len(self.cards)):
            if self.cards[ii]==card:
                return ii
        return -1
    def removeCard(self,card):
        icard=self.findCard(card)
        if not icard==None:
            self.playedcards.append(self.cards.pop(icard))
    def faceUp(self):
        [card.faceUp() for card in self.cards]
    def faceDown(self):
        [card.faceDown() for card in self.cards]
    def sort(self):
        self.cards=UTILITIES.sortCards(self.cards)

