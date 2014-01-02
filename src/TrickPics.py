import pygame
from Globals import COLORS,DECKDEFS,UTILITIES
class TrickPics():
    def __init__(self,screen):
        screct=screen.get_rect()
        self.nseats       =DECKDEFS.nseats
        self.cardrect     =DECKDEFS.backimage.get_rect()
        self.smallcardrect=DECKDEFS.smallimages[0].get_rect()
        self.currentsize =(self.cardrect.width*2+10,self.cardrect.height*5/3+10)
        self.previoussize=(self.smallcardrect.width*2+10,self.smallcardrect.height*5/3+10)
        #self.currentpos =(screct.centerx-self.cardrect.width/2,screct.centery-self.cardrect.height/2)
        #self.previouspos=(screct.right-self.smallcardrect.width,screct.top)
        self.currentpos =(screct.centerx-self.currentsize[0]/2,screct.centery-self.currentsize[1]/2)
        self.previouspos=(screct.right-self.previoussize[0]-4,screct.top+4)
        self.currentsurf =pygame.Surface(self.currentsize,1).convert()
        self.previoussurf=pygame.Surface(self.previoussize,1).convert()
        self.currentrect =self.currentsurf.get_rect()
        self.previousrect=self.previoussurf.get_rect()
        self.currentx=[0,self.cardrect.width/2,0,-self.cardrect.width/2]
        self.currenty=[self.cardrect.height/3,0,-self.cardrect.height/3,0]
        self.previousx=[0,self.smallcardrect.width/2,0,-self.smallcardrect.width/2]
        self.previousy=[self.smallcardrect.height/3,0,-self.smallcardrect.height/3,0]
        self.prevarrowpos=((0,-59),(55,0),(0,59),(-55,0)) #NABOHACK
        self.prevarrowsurf=pygame.Surface((8,8),1).convert()
        self.prevarrowrect=self.prevarrowsurf.get_rect()
        self.currarrowpos=((0,-95),(90,0),(0,95),(-90,0)) #NABOHACK
        self.currarrowsurf=pygame.Surface((10,10),1).convert()
        self.currarrowrect=self.currarrowsurf.get_rect()
    def clearCurrent(self,screen):
        self.currentsurf.fill(COLORS['tablelight'])
        self.drawArrowsCurrent(screen,None,True)
        screen.blit(self.currentsurf,self.currentpos)
    def clearPrevious(self,screen):
        self.previoussurf.fill(COLORS['table'])
        self.drawArrowsPrevious(screen,None,True)
        screen.blit(self.previoussurf,self.previouspos)
    def drawCurrent(self,screen,trick):
        if trick==None:
            return
        self.clearCurrent(screen)
        rect=self.currentrect
        x=self.currentx
        y=self.currenty
        for icard in range(len(trick.cards)):
            ipos=(icard+trick.leadseat)%self.nseats
            self.cardrect.center=(rect.centerx+x[ipos],rect.centery-y[ipos])
            trick.cards[icard].faceUp()
            trick.cards[icard].draw(self.currentsurf,self.cardrect.topleft)
        screen.blit(self.currentsurf,self.currentpos)
        self.drawArrowsCurrent(screen,trick)
    def drawPrevious(self,screen,trick):
        if trick==None:
            return
        self.clearPrevious(screen)
        rect=self.previousrect
        x=self.previousx
        y=self.previousy
        for icard in range(len(trick.cards)):
            ipos=(icard+trick.leadseat)%self.nseats
            self.smallcardrect.center=(rect.centerx+x[ipos],rect.centery-y[ipos])
            trick.cards[icard].faceUp()
            trick.cards[icard].drawFaceUpSmall(self.previoussurf,self.smallcardrect.topleft)
        screen.blit(self.previoussurf,self.previouspos)
        self.drawArrowsPrevious(screen,trick)
    def getCurrentArrowPos(self,screen,iseat):
        screenrect=screen.get_rect()
        pos=[screenrect.centerx,screenrect.centery]
        pos[0]+=(self.currarrowpos[iseat])[0]-self.currarrowrect.width/2
        pos[1]+=(self.currarrowpos[iseat])[1]-self.currarrowrect.height/2
        return pos
    def drawArrowsCurrent(self,screen,trick,clear=False):
        screenrect=screen.get_rect()
        for iseat in range(DECKDEFS.nseats):
            self.currarrowsurf.fill(COLORS['table'])
            if not clear:
                if iseat==trick.nextSeatInd():
                    UTILITIES.drawArrowHead(self.currarrowsurf,COLORS['yellow'],('d','l','u','r')[(iseat+2)%4])
            screen.blit(self.currarrowsurf,self.getCurrentArrowPos(screen,iseat))
    def drawArrowsPrevious(self,screen,trick,clear=False):
        screenrect=screen.get_rect()
        for iseat in range(DECKDEFS.nseats):
            self.prevarrowsurf.fill(COLORS['table'])
            if not clear:
                if iseat==trick.leadseat:
                    UTILITIES.drawArrowHead(self.prevarrowsurf,COLORS['yellow'],('d','l','u','r')[(iseat+2)%4])
            x=self.previouspos[0]+self.previoussize[0]/2+self.prevarrowpos[iseat][0]-self.prevarrowrect.width/2
            y=self.previouspos[1]+self.previoussize[1]/2+self.prevarrowpos[iseat][1]-self.prevarrowrect.height/2
            screen.blit(self.prevarrowsurf,(x,y))
    def draw(self,screen,current,previous):
        self.drawCurrent(screen,current)
        self.drawPrevious(screen,previous)
    def clear(self,screen):
        self.clearCurrent(screen)
        self.clearPrevious(screen)

