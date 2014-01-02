import types,pygame,time,AI
from Rubber import Rubber
from InfoBoxes import InfoBoxes
from Effects import EFFECTS
from Globals import UTILITIES,COLORS,DECKDEFS
class Table(Rubber):
    def __init__(self,screen):
        self.auto=False#True
        Rubber.__init__(self,screen)
        self.showallhands=True
        screen.fill(COLORS['table'])
        EFFECTS.drawSimpleIntro(screen)
        #BEEPS.beep[0].play()
        beep=pygame.mixer.Sound("../snd/beep1.ogg")
        beep.play()
        self.info=InfoBoxes(screen)
        self.clear(screen)
        self.faceUp()
        if not self.auto:
            UTILITIES.pressAnyKey(screen)
    def clear(self,screen):
        self.info.trickpics.clear(screen)
        Rubber.clear(self,screen)
    def toggleShowAllHands(self,screen):
        if self.showallhands:
            self.showallhands=False
        else:
            self.showallhands=True
        self.setVisibility()
        self.draw(screen)
    def getVisible(self,seat):
        if self.showallhands:
            return True
        if seat.human or seat.dummy:
            return True
        elif seat.humanspartner:
            partner=self.getPartner(seat)
            if partner.contractowner:
                return True
        return False
    def setVisibility(self):
        for seat in self.getHands():
            if self.getVisible(seat):
                seat.faceUp()
            else:
                seat.faceDown()
    def getPlayable(self,seat):
        return self.getVisible(seat)
    def drawTricks(self,screen):
        current=self.currentTrick()
        previous=self.previousTrick()
        self.info.trickpics.draw(screen,current,previous)
    def newHand(self,screen):
        self.info.updateTrickCount(screen,None)
        self.info.updateContract(screen,None)
        self.info.trickpics.clear(screen)
#        self.shuffle()
#        self.setVisibility()
        while True:
            Rubber.newHand(self,screen)
            self.drawAnime(screen)
            self.info.updateDealer(screen,self.dealer)
            self.getContract(screen,self,self.auto)
            if self.contract:
                break
        self.info.updateContract(screen,self.contract)
        self.info.updateTrickCount(screen,(0,0))
        self.setVisibility()
        if not self.auto:
            UTILITIES.pressAnyKey(screen)
        self.bidding.historybox.hide(screen)
#        self.drawTricks(screen)
    def playRubber(self,screen):
        self.zeroScore()
        self.info.score.clear(screen)
        while True:
            self.newHand(screen)
            self.processCardPlay(screen)
            keepgoing=self.endHand()
            self.info.score.draw(screen,self.score)
            pygame.display.flip()
            if not self.auto:
                UTILITIES.pressAnyKey(screen) 
            if not keepgoing:
                break
    def playCard(self,screen,card):
        Rubber.playCard(self,screen,card,self.auto)
        self.drawTricks(screen)
        self.info.updateTrickCount(screen,self.trickcount)
        pygame.display.flip()
    def userSelectCard(self,screen):
        mousepos=pygame.mouse.get_pos()
        seat=self.getNextSeat()
        if seat.rect.collidepoint(mousepos):
            if self.getPlayable(seat):
                card=seat.getCard(mousepos)
                self.playCard(screen,card)
    def getUserCard(self,screen):
        ctrldown=False
        mouseDown=(0,0,0)
        pygl=pygame.locals
        while True:
            #for event in pygame.event.get():
            if True:
                event=pygame.event.wait()
                if UTILITIES.globalShortcuts(event,ctrldown):
                    continue
                etype=event.type
                if etype==pygl.KEYDOWN:
                    if event.key==pygl.K_LCTRL or event.key==pygl.K_RCTRL:
                        ctrldown=True
#                    if (event.key==pygl.K_q or event.key==pygl.K_c) and ctrldown:
#                        GLOBALS.util.quit()
                    elif event.key==pygl.K_i:
                        self.showHandsInfo(screen)
                    elif event.key==pygl.K_b:
                        self.bidding.historybox.transient(screen)
#                    elif event.key==pygl.K_s:
#                        self.scorebox.transient(screen)
                elif etype==pygl.KEYUP:
                    if event.key==pygl.K_LCTRL or event.key==pygl.K_RCTRL:
                        ctrldown=False
                elif etype==pygl.MOUSEBUTTONDOWN:
                    mouseDown=pygame.mouse.get_pressed()
                elif etype==pygl.MOUSEBUTTONUP:
                    if mouseDown[0]==True:
                        mousepos=pygame.mouse.get_pos()
                        seat=self.getNextSeat()
                        if seat.rect.collidepoint(mousepos):
                            if self.getPlayable(seat):
                                card=seat.getCard(mousepos)
                                if type(card) is not types.NoneType:
                                    return card
                    mouseDown=(0,0,0)
    def showHandsInfo(self,screen):
        oldsurf=screen.copy()
        for ihand in range(DECKDEFS.nseats):
            hand=self.getHand(ihand)
            if not self.getVisible(hand):#table.rubber.deal.getHand(ihand)):
                continue
            handinfo=hand.info#self.handinfo[ihand]
            screen.blit(handinfo.surf,handinfo.rect.topleft)
            pygame.display.flip()
        UTILITIES.pause()
        screen.blit(oldsurf,(0,0))
        pygame.display.flip()
    def processCardPlay(self,screen):
        while self.playable():
            if not self.auto and self.getNextSeat().human:
                card=self.getUserCard(screen)
            else:
                card=AI.chooseCard(self)
            self.playCard(screen,card)


