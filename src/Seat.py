import pygame,time
from Hand import Hand
from TextBox import TextBox
from Globals import COLORS,DECKDEFS
from Effects import EFFECTS
class Seat(Hand):
    def __init__(self,screen,seat,cards):
        Hand.__init__(self,cards)
        self.name=seat[0].lower()
        self.human=False
        self.dummy=False
        self.humanspartner=False
        self.contractowner=False
        self.bgcolor=COLORS['tablelight']
        self.orient='h'
        self.winsize=[373,370]
#        self.winsize=[cs[0]+12*self.dx,cs[1]+12*self.dy]
        self.x,self.y,self.dx,self.dy=10,10,25,25
        sr=screen.get_rect()
        cs=DECKDEFS.cardsize
        seatx=[sr.centerx, sr.right-cs[0]/2,  sr.centerx,        cs[0]/2]
        seaty=[cs[1]/2,    sr.bottom-self.winsize[1]/2, sr.bottom-cs[1]/2, sr.bottom-self.winsize[1]/2]
        for iseat in range(len(DECKDEFS.seats)):
            if self.name==DECKDEFS.seats[iseat].lower()[0]:
                self.orient=('h','v')[iseat%2]
                self.x=seatx[iseat]
                self.y=seaty[iseat]
                break
        if self.orient=='v':
            self.surf=pygame.Surface((cs[0],self.winsize[1]),1).convert()
        else:
            self.surf=pygame.Surface((self.winsize[0],cs[1]),1).convert()
        self.rect=self.surf.get_rect()
        self.rect.centerx=self.x
        self.rect.centery=self.y
        self.clear(screen)
        w,h=75,75
        if self.name=='n':
            x=sr.centerx-w/2
            y=cs[1]
            self.offset=(0,-10)
        elif self.name=='e':
            x=sr.right-w-cs[0]
            y=sr.centery-h/2
            self.offset=(-10,0)
        elif self.name=='s':
            x=sr.centerx-w/2
            y=sr.bottom-cs[1]-h
            self.offset=(0,10)
        elif self.name=='w':
            x=cs[0]
            y=sr.centery-h/2
            self.offset=(10,0)
#        self.info=TextBox(None,(x,y),(w,h),14,COLORS['tablelight'],COLORS['yellow'])
        self.info=TextBox(None,(x,y),(w,h),14,COLORS['grey'],COLORS['yellow'])
        self.info.centeredy=False
        self.updateInfo()
    def updateInfo(self):
        self.info.erase()
        data=[" HC = "+str(self.HCP),
              " DP = "+str(self.DP),
              " QT = "+str(self.QT),
              " NL = "+str(self.NL)]
        self.info.update(data)
    def setCards(self,cards):
        Hand.setCards(self,cards)
        Seat.updateInfo(self)
    def clear(self,screen):
        self.surf.fill(self.bgcolor)
        screen.blit(self.surf,self.rect.topleft)
    def getCardIndex(self,screenpos):
        seatpos=(screenpos[0]-self.rect.left,screenpos[1]-self.rect.top)
        for icard in range(len(self.cards)):
            ireverse=len(self.cards)-icard-1
            rect=pygame.Rect(self.getCardPos(ireverse),DECKDEFS.cardsize)
            if rect.collidepoint(seatpos):
                return ireverse
        return None
    def getCard(self,screenpos):
        index=self.getCardIndex(screenpos)
        if index==None:
            return None
        else:
            return self.cards[index]
    def playCard(self,screen,card,auto=False):
        icard=self.findCard(card)
        self.removeCard(card)
        self.clear(screen)
        self.draw(screen)
        screencenter=screen.get_rect().center
        pos0=self.getCardPosPicked(icard)
        pos1=(screencenter[0]-DECKDEFS.cardsize[0]/2,screencenter[1]-DECKDEFS.cardsize[1]/2)
        if not auto:
            EFFECTS.drawTrace(screen,card.img,pos0,pos1,30,0,24)
    def getCardPos(self,icard):
        if self.orient=='v':
            return (0,self.dy*icard)
        else:
            return (self.dx*icard,0)
    def getCardAbsPos(self,icard):
        relpos=self.getCardPos(icard)
        seatpos=(self.rect.left,self.rect.top)
        return (seatpos[0]+relpos[0],seatpos[1]+relpos[1])
    def getCardPosPicked(self,icard):
        (x0,y0)=self.getCardAbsPos(icard)
        return (x0+self.offset[0],y0+self.offset[1])
    def drawOneCard(self,screen,icard):
        pos=self.getCardPos(icard)
        self.cards[icard].draw(self.surf,pos)
        screen.blit(self.surf,self.rect)
        pygame.display.flip()
    def draw(self,screen,motion=True):
        for icard in range(len(self.cards)):
            pos=self.getCardPos(icard)
            self.cards[icard].draw(self.surf,pos)
        screen.blit(self.surf,self.rect)

