import pygame
from Score import Score
from TextBox import TextBox
from ScoreBox import ScoreBox
from TrickPics import TrickPics
from Globals import COLORS,DECKDEFS,UTILITIES
class InfoBoxes:
    def __init__(self,screen):
        screenrect=screen.get_rect()
        bgcolor=COLORS['tabledark']
        fgcolor=COLORS['yellow']
        helpdata=['','Bridget 0.1',
        '--------------------------------',
        'F1/ctrl+H - Show Help',
        'F5/ctrl+N - New Rubber',
        'F9 - Toggle Show All Hands',
        'B - Show/Hide Bidding',
        'Mouse - select card','ESC - Quit',
        '--------------------------------']
        self.help=      TextBox(helpdata,      None,   (400,300),18,COLORS['black'],COLORS['yellow'])
        self.contract=  TextBox(['Contract:'],(10,125),None,     14,bgcolor,fgcolor)
        self.trickcount=TextBox(['Tricks:'],  (10,145),None,     14,bgcolor,fgcolor)
        self.dealer=    TextBox(['Dealer:'],  (10,105),None,     14,bgcolor,fgcolor)
        self.score=ScoreBox(screen)
        self.trickpics=TrickPics(screen)
        self.handinfo=[]
      #  size=(125,80)
      #  pos=(50,160) 
      #  for iseat in range(GLOBALS.deck.nseats):
      #      self.handinfo.append(TextBox(None,pos,size,14,GLOBALS.colors['black'],GLOBALS.colors['yellow']))
        self.help.centered=1
        self.help.alpha=200
        self.help.update()
        self.draw(screen)
    def showHandsInfo(self,screen,table):
        surf=screen.copy()
        for ihand in range(DECKDEFS.nseats):
            if not table.getVisible(table.rubber.deal.getHand(ihand)):
                continue
            handinfo=self.handinfo[ihand]
            screen.blit(handinfo.surf,handinfo.rect.topleft)
            pygame.display.flip()
        UTILITIES.pause()
        screen.blit(surf,(0,0))
    def drawHandsInfo(self,deal):
        for ihand in range(DECKDEFS.nseats):
            hand=deal.getHand(ihand)
            self.handinfo[ihand].erase()
            data=[hand.HCP,hand.DP,hand.QT,hand.NL]
            self.handinfo[ihand].update(data)
    def draw(self,screen):
        self.trickcount.draw(screen)
        self.contract.draw(screen)
        self.dealer.draw(screen)
    def updateTrickCount(self,screen,trickcount):
        data=['Tricks:       ']
        if not trickcount==None:
            data[0]+='%i - %i'%(trickcount[0],trickcount[1])
        self.trickcount.draw(screen,data)
    def updateContract(self,screen,contract=None):
        self.contract.surf.fill(self.contract.colorbg)
        data='Contract:   '
        if contract:
            data+=DECKDEFS.seats[contract.owner]
        img1=self.contract.font.render(data,1,self.contract.colorfg)
        rect=img1.get_rect()
        rect.centery=self.contract.surf.get_rect().centery
        rect.left=2
        self.contract.surf.blit(img1,rect.topleft)#(2,0))
        if contract:
            pos=(img1.get_rect().width+25,8)
            UTILITIES.blitBid(self.contract.font,self.contract.surf,contract,self.contract.colorfg,pos,True)
        self.contract.show(screen)
    def updateDealer(self,screen,dealer):
        if not dealer==None:
            data=['Dealer:      '+DECKDEFS.seats[dealer]]
        self.dealer.draw(screen,data)

