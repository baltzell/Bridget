import pygame
from Box import Box
from Globals import COLORS,FONTS,DECKDEFS,UTILITIES
class BiddingHistoryBox(Box):
    def __init__(self,screen):
        self.dx=45
        self.dy=25
        self.colorfg=COLORS['black']
        self.font=FONTS[12]
        screct=screen.get_rect()
        self.maxrows=8
        self.size=[self.dx*DECKDEFS.nseats,self.dy*self.maxrows]
        self.pos=(screct.right-DECKDEFS.cardsize[0]-self.size[0]-10,screct.centery-90)
        Box.__init__(self,self.size,self.pos,COLORS['white'])
        self.visible=False
        self.drawHeaders(screen)
    def drawHeaders(self,screen):
        for ix in range(len(DECKDEFS.seats)):
            img=self.font.render((DECKDEFS.seats[ix])[0],1,self.colorfg)
            imgrect=img.get_rect()
            imgrect.centerx=(2*ix+1)*self.dx/2
            imgrect.centery=self.dy/2
            self.surf.blit(img,imgrect.topleft)
        screen.blit(self.surf,self.rect.topleft)
    def addBid(self,screen,bidding):
        bid=bidding.bids[len(bidding.bids)-1]
        ix=bid.owner
        iy=int((len(bidding.bids)-1+bidding.openingseat)/DECKDEFS.nseats)+1
        x=(2*ix+1)*self.dx/2
        y=(2*iy+1)*self.dy/2
        UTILITIES.blitBid(self.font,self.surf,bid,self.colorfg,(x,y))
        self.show(screen)
    def reset(self,screen):
        self.erase()
        self.drawHeaders(screen)

