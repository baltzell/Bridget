import pygame
from Box import Box
from Bid import Bid
from Globals import DECKDEFS,COLORS,FONTS,UTILITIES
class BiddingBox(Box):
    def __init__(self,screen):
        butsz=(40,30)
        nbut=(DECKDEFS.ntrumps,8)
        self.size=(butsz[0]*nbut[0],butsz[1]*nbut[1])
        self.pos=(DECKDEFS.cardsize[0]+5,screen.get_rect().centery-90)
        self.font=FONTS[12]
        self.buttoncolor=COLORS['white']
        self.fgcolor=COLORS['black']
        Box.__init__(self,self.size,self.pos,COLORS['lightred'])
        self.rects=[]
        self.bids=[]
        for itrump in range(DECKDEFS.ntrumps):
            for ilevel in range(7):
                pos=(itrump*butsz[0],ilevel*butsz[1])
                self.addBid(Bid(ilevel+1,itrump),pos,butsz)
        self.addBid(Bid(1),(0*butsz[0],7*butsz[1]),butsz)
        self.addBid(Bid(2),(1*butsz[0],7*butsz[1]),butsz)
        self.addBid(Bid(0),(2*butsz[0],7*butsz[1]),(butsz[0]*3,butsz[1]))
    def reset(self,screen):
        self.erase()
        self.rects=[]
        self.bids=[]
        for itrump in range(DECKDEFS.ntrumps):
            for ilevel in range(7):
                pos=(itrump*butsz[0],ilevel*butsz[1])
                self.addBid(Bid(ilevel+1,itrump),pos,butsz)
        self.addBid(Bid(1),(0*butsz[0],7*butsz[1]),butsz)
        self.addBid(Bid(2),(1*butsz[0],7*butsz[1]),butsz)
        self.addBid(Bid(0),(2*butsz[0],7*butsz[1]),(butsz[0]*3,butsz[1]))
    def disallowBid(self,bid):
        pass
    def addBid(self,bid,pos,size):
        self.bids.append(bid)
        rect=pygame.Rect(pos,size)
        self.rects.append(rect)
        insize=(size[0]-2,size[1]-2)
        inpos=(pos[0]+2,pos[1]+2)
        surf=pygame.Surface(insize,1).convert()
        surf.fill(self.buttoncolor)
        surfrect=surf.get_rect()
        UTILITIES.blitBid(self.font,surf,bid,self.fgcolor,surfrect.center)
        self.surf.blit(surf,inpos)
    def getBid(self,screenpos):
        bboxpos=(screenpos[0]-self.rect.left,screenpos[1]-self.rect.top)
        for ibid in range(len(self.bids)):
            if self.rects[ibid].collidepoint(bboxpos):
                return self.bids[ibid]
        return None

