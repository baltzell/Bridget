from Globals import DECKDEFS
class Trick():
    def __init__(self,leadseat,trump):
        self.cards=[]
        self.leadseat=leadseat
        self.trump=trump
        self.wincard=None
        self.leadsuit=None
        self.winseat=leadseat
        self.nseats=DECKDEFS.nseats
    def nextSeatInd(self):
        if len(self.cards)==0:
            return self.leadseat
        elif len(self.cards)>=self.nseats:
            return self.winseat
        else:
            return (self.leadseat+len(self.cards))%self.nseats
    def addCard(self,card):
        if len(self.cards)<self.nseats:
            self.cards.append(card)
            if len(self.cards)==1:
                self.wincard=card
                self.leadsuit=card.isuit
            else:
                self.winner()
            return True
        else:
            return False
    def winner(self):
        inewcard=len(self.cards)-1
        newcard=self.cards[inewcard]
        newseat=(inewcard+self.leadseat)%self.nseats
        if newcard.isuit==self.wincard.isuit:
            if newcard.irank>self.wincard.irank:
                self.wincard=newcard
                self.winseat=newseat
        elif newcard.isuit==self.trump:
            self.wincard=newcard
            self.winseat=newseat

