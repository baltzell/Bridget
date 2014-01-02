import random
from Card import Card
from Trick import Trick
from Seat import Seat
from Globals import DECKDEFS
class Deal:
    def __init__(self,screen):
        self.cards=[]
        for index in range(DECKDEFS.ncards):
            self.cards.append(Card(index,None))
        nr=DECKDEFS.nranks
        self.north=Seat(screen,'n',self.cards[0*nr:1*nr])
        self.east =Seat(screen,'e',self.cards[1*nr:2*nr])
        self.south=Seat(screen,'s',self.cards[2*nr:3*nr])
        self.west =Seat(screen,'w',self.cards[3*nr:4*nr])
        self.south.human=True
        self.north.humanspartner=True
        self.tricks=[]
        self.trickcount=[0,0]
        self.contract=None
    def playable(self):
        ntricks=len(self.tricks)
        if ntricks>12:
            if len(self.tricks[ntricks-1].cards)>3:
                return False
        return True
    def getNextSeatInd(self):
        if len(self.tricks)==0:
            return (self.contract.owner+1)%DECKDEFS.nseats
        else:
            return self.tricks[len(self.tricks)-1].nextSeatInd()
    def getNextSeat(self):
        return (self.getHands())[self.getNextSeatInd()]
    def currentTrick(self):
        if len(self.tricks)>0:
            return self.tricks[len(self.tricks)-1]
        else:
            return None
    def previousTrick(self):
        if len(self.tricks)>1:
            return self.tricks[len(self.tricks)-2]
        else:
            return None
    def shuffle(self):
        random.shuffle(self.cards)
        self.setHands()
        self.trickcount=[0,0]
        self.tricks=[]
        self.contract=None
    def setHands(self):
        nr=DECKDEFS.nranks
        self.north.setCards(self.cards[0*nr:1*nr])
        self.east.setCards( self.cards[1*nr:2*nr])
        self.south.setCards(self.cards[2*nr:3*nr])
        self.west.setCards( self.cards[3*nr:4*nr])
    def sortHands(self):
        for seat in self.getHands():
            seat.sort()
    def faceUp(self):
        for seat in self.getHands():
            seat.faceUp()
    def faceDown(self):
        for seat in self.getHands():
            seat.faceDown()
    def getHands(self):
        return [self.north,self.east,self.south,self.west]
    def getHand(self,hand):
        if type(hand) is int:
            iseat=hand
        else:
            iseat=DECKDEFS.seats1.index(seat[0].lower())
        return (self.getHands())[iseat]
    def findHand(self,card):
        for seat in self.getHands():
            icard=seat.findCard(card)
            if not icard==None:
                return seat
        return None
    def drawAnime(self,screen):
        self.clear(screen)
        for irank in range(DECKDEFS.nranks):
            self.north.drawOneCard(screen,irank)
            self.east.drawOneCard(screen,irank)
            self.south.drawOneCard(screen,irank)
            self.west.drawOneCard(screen,irank)
    def draw(self,screen):
        for seat in self.getHands():
            seat.clear(screen)
            seat.draw(screen)
    def clear(self,screen):
        for seat in self.getHands():
            seat.clear(screen)
    def playCard(self,screen,card,auto=False):
        if len(self.tricks)==0:
            leadseat=self.getNextSeatInd()
            self.tricks.append(Trick(leadseat,self.contract.trump))
        seat=self.findHand(card)
        seat.playCard(screen,card,auto)
        self.tricks[len(self.tricks)-1].addCard(card)
        trick=self.tricks[len(self.tricks)-1]
        if len(trick.cards)>3:
            self.trickcount[trick.winseat%2]+=1
            if len(self.tricks)<13:
                self.tricks.append(Trick(trick.winseat,self.contract.trump))
    def getLHO(self,seat):
        if type(seat) is str:
            seat=DECKDEFS.seats1.index(seat[0].lower())
        return self.getHand((seat+3)%4)
    def getRHO(self,seat):
        if type(seat) is str:
            seat=DECKDEFS.seats1.index(seat[0].lower())
        return self.getHand((seat+1)%4)
    def getPartner(self,seat):
        if type(seat) is int:
            iseat=seat
        elif type(seat) is str:
            iseat=DECKDEFS.seats1.index(seat[0].lower())
        else:
            iseat=DECKDEFS.seats1.index(seat.name)
        return self.getHand((iseat+2)%4)

