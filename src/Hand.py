from CardGroup import CardGroup
from Globals import DECKDEFS
class Hand(CardGroup):
    def __init__(self,cards):
        CardGroup.__init__(self,cards)
        Hand.updateInfo(self)
    def updateInfo(self):
        self.HCP=self.HighCardPoints()
        self.DP=self.DistributionPoints()
        self.NL=self.Nlosers()
        self.QT=self.QuickTricks()
    def setCards(self,cards):
        CardGroup.setCards(self,cards)
        Hand.updateInfo(self)
    def Suit(self,suit):
        newcards=[]
        for card in self.cards:
            if type(suit) is int:
                if card.isuit==suit:
                    newcards.append(card)
            else:
                if card.suit[0].lower()==suit[0].lower():
                    newcards.append(card)
        return newcards
    def Suits(self):
        suits=[]
        for isuit in range(DECKDEFS.nsuits):
            suits.append(self.Suit(isuit))
        return suits
    def Rank(self,rank):
        newcards=[]
        for card in self.cards:
            if type(rank) is int:
                if card.irank==rank:
                    newcards.append(x)
            else:
                if card.rank[0].lower()==rank[0].lower():
                    newcards.append(x)
        return newcards
    def Nrank(self,rank):
        return len(self.Rank(rank))
    def Nsuit(self,suit):
        return len(self.Suit(suit))
    def SuitLow(self,suit):
        cards=self.Suit(suit)
        if len(cards)>0:
            return cards[len(cards)-1]
        return None
    def SuitHigh(self,suit):
        cards=self.Suit(suit)
        if len(cards)>0:
            return cards[0]
        return None
    def JustHighEnough(self,trick):
        irank2beat=trick.wincard.irank
        cards=self.Suit(trick.wincard.isuit)
        ncards=len(cards)
        if ncards>0:
#            if cards[0].irank>irank2beat:
            for icard in range(len(cards)):
                if cards[icard].irank<irank2beat:
                    return cards[icard-1]
        return None
    def LongestSuit(self):
        longest=-1
        length=0
        for isuit in range(DECKDEFS.nsuits):
            nsuit=self.Nsuit(isuit)
            if nsuit>length:
                length=nsuit
                longest=isuit
        return longest
    def LowestOfLongest(self):
        suit=self.LongestSuit()
        cards=self.Suit(suit)
        return cards[len(cards)-1]
    def FourthLowestOfLongest(self):
        suit=self.LongestSuit()
        cards=self.Suit(suit)
        if len(cards)<4:
            return cards[len(cards)-1]
        else:
            return cards[3]
    def Lowest(self):
        for irank in range(DECKDEFS.nranks):
            cards=self.Rank(irank)
            if len(cards)==0:
                continue
            elif len(cards)==1:
                return cards[0]
            else:
                longest=-1
                length=0
                for card in cards:
                    nsuit=self.Nsuit(card.isuit)
                    if nsuit>length:
                        longest=card.isuit
                        length=nsuit
                for card in cards:
                    if card.isuit==longest:
                        return card
    def Naces(self):
        return self.Nrank('a')
    def Nkings(self):
        return self.Nrank('k')
    def Nqueens(self):
        return self.Nrank('q')
    def Nlosers(self):
        nlosers=0
        for isuit in range(DECKDEFS.nsuits):
            nsuitlosers=0
            for irank in range(DECKDEFS.nranks-1,0,-1):
                index=irank+isuit*DECKDEFS.nranks
                if not self.findCard(index)==None or nsuitlosers>1:
                    break
                else:
                    nsuitlosers+=1
                    nlosers+=1
        return nlosers
    def HighCardPoints(self):
        hcp=0
        for card in self.cards:
            if card.irank>8:
                hcp+=card.irank-8
        return hcp
    def DistributionPoints(self):
        dp=0
        for suit in DECKDEFS.suits:
            ncards=self.Nsuit(suit)
            if ncards<3:
                dp+=3-ncards
        return dp
    def QuickTricks(self):
        qt,ace,king=0,False,False
        newsuit=[True,True,True,True]
        for card in self.cards:
            rank=card.rank[0].lower()
            nsuit=self.Nsuit(card.isuit)
            if newsuit[card.isuit]==True:
                ace,king=False,False
                newsuit[card.isuit]=False
            if rank=='a':
                ace=True
                qt+=1
            elif rank=='k':
                king=True
                if nsuit>1 and nsuit<7:
                    if ace==True:
                        qt+=1
                    else:
                        qt+=0.5
            elif rank=='q':
                if nsuit<6 and (ace==True or king==True):
                    qt+=0.5
        return qt
    def CanBeat(self,trick):
        print 'canbeat?'
        if len(trick.cards)==0:
            return True
        myleadsuit=self.Suit(trick.leadsuit)
        if len(myleadsuit)>0:
            if trick.wincard.suit==trick.cards[0].suit:#leadsuit:
                for card in myleadsuit:
                    print card.irank,trick.wincard.irank
                    if card.irank>trick.wincard.irank:
                        print 'good'
                        return True
        elif trick.trump:
            mytrumps=self.Suit(trick.trump)
            if len(mytrumps)>0:
                if trick.wincard.suit!=trick.trump:
                    return True
                else:
                    for card in mytrumps:
                        if card.irank>trick.wincard.irank:
                            return True
        return False

