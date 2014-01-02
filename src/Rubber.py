from Bidding import Bidding
from Deal import Deal
from Score import Score
class Rubber(Deal):
    def __init__(self,screen):
        Deal.__init__(self,screen)
        self.dealer=-1
        self.bidding=Bidding(screen,self.dealer)
        self.score=Score()
        self.contract=None
    def newHand(self,screen):
        self.contract=None
        self.shuffle()
        self.rotateDealer()
        self.bidding.reset(screen,self.dealer)
    def getContract(self,screen,table,auto):
        self.bidding.processBidding(screen,table,auto)
        self.contract=self.bidding.contract
        if self.contract:
            self.getHand(self.contract.owner).contractowner=True
    def rotateDealer(self):
        self.dealer=(self.dealer+1)%4
    def endHand(self):
        return self.score.addScore(self.contract,self.trickcount)
    def zeroScore(self):
        self.games=[0,0]
        for xx in self.score.scores:
            xx.over=0
            xx.under=[0]


