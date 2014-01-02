import pygame, AI
from Bid import Bid
from BiddingBox import BiddingBox
from BiddingHistoryBox import BiddingHistoryBox
from Globals import DECKDEFS, UTILITIES
class Bidding():
    def __init__(self,screen,openingseat):
        self.bids=[]
        self.contract=None
        self.openingseat=openingseat
        self.imaxbid=-1
        self.passesinarow=0
        self.box=BiddingBox(screen)
        self.historybox=BiddingHistoryBox(screen)
    def partnerHasBid(self):
        return False
    def opponentsHaveBid(self):
        return False
    def getOpponentsBids(self):
#        for bid in self.bids:
#            if bid.owner
        pass
    def nextSeatInd(self):
        if len(self.bids)==0:
            return self.openingseat
        else:
            return (self.openingseat+len(self.bids))%DECKDEFS.nseats
    def reset(self,screen,openingseat):
        self.bids=[]
        self.contract=None
        self.openingseat=openingseat
        self.imaxbid=-1
        self.passesinarow=0
        self.historybox.reset(screen)
    def getUserBid(self,screen,table):
        ctrldown=False
        mouseDown=(0,0,0)
        pygl=pygame.locals
        while True:
            #for event in pygame.event.wait():
            event=pygame.event.wait()
            if event:
                if UTILITIES.globalShortcuts(event,ctrldown):
                    continue
                etype=event.type
                if etype==pygl.KEYDOWN:
                    if event.key==pygl.K_LCTRL or event.key==pygl.K_RCTRL:
                        ctrldown=True
                    elif event.key==pygl.K_i:
                        table.showHandsInfo(screen)
                elif etype==pygl.KEYUP:
                    if event.key==pygl.K_LCTRL or event.key==pygl.K_RCTRL:
                        ctrldown=False
                elif etype==pygl.MOUSEBUTTONDOWN:
                    mouseDown=pygame.mouse.get_pressed()
                elif etype==pygl.MOUSEBUTTONUP:
                    if mouseDown[0]==True:
                        mousepos=pygame.mouse.get_pos()
                        if self.box.rect.collidepoint(mousepos):
                            return self.box.getBid(mousepos)
                    mouseDown=(0,0,0)
    def processBidding(self,screen,table,auto):
        self.bids=[]
        self.contract=None
        self.imaxbid=-1
        self.passesinarow=0
        self.box.show(screen)
        self.historybox.reset(screen)
        pygame.display.flip()
        biddingdone=0
        while biddingdone>=0:
            nextseatind=self.nextSeatInd()
            if not auto and table.getHand(nextseatind).human:
                bid=self.getUserBid(screen,table)
            else:
                bid=AI.chooseBid(table)
            if bid:
                biddingdone=self.addBid(bid)
                if biddingdone!=0:
                    self.historybox.addBid(screen,self)
                    pygame.display.flip()
        self.box.hide(screen)
    def checkDouble(self,double):
        # NABO
        return 0
    def addBid(self,bid):
        goodbid=0
        bid.owner=(len(self.bids)+self.openingseat)%DECKDEFS.nseats
        if bid.level==0:
            self.bids.append(bid)
            self.passesinarow+=1
            goodbid=1
        elif bid.trump==None:
            if self.imaxbid>=0:
                if self.checkDouble(bid.double):
                    self.bids[self.imaxbid].double=bid.double
                    self.bids.append(bid)
                    self.passesinarow=0
                    goodbid=1
        elif self.imaxbid<0:
            self.imaxbid=len(self.bids)
            self.bids.append(bid)
            self.passesinarow=0
            goodbid=1
        elif bid.value>self.bids[self.imaxbid].value:
            self.imaxbid=len(self.bids)
            self.bids.append(bid)
            self.passesinarow=0
            goodbid=1
        if self.passesinarow==3:
            if self.imaxbid>=0:
                self.contract=self.bids[self.imaxbid]
                self.contract.owner=(self.imaxbid+self.openingseat)%DECKDEFS.nseats
                goodbid=-1
        elif self.passesinarow>3:
            if self.imaxbid<0:
                goodbid=-1
        return goodbid

