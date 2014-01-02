#!/usr/bin/env python
import os,pygame
from Table import Table
from Globals import UTILITIES
class Bridget:
    def __init__(self,screen):
        self.screen=screen
        self.table=Table(self.screen)
        while True:
            self.table.playRubber(self.screen)
            UTILITIES.pressAnyKey(screen)
    def loop(self):
        self.ctrlDown=False
#        self.mouseDown=(0,0,0)
        while 1:
#            for event in pygame.event.get():
            #event=pygame.event.wait()
            #if not self.processEvent(event):
            #    return
            self.processEvent(pygame.event.wait())
            pygame.display.flip()
    def processEvent(self,event):
        if UTILITIES.globalShortcuts(event,self.ctrlDown):
            return
        elif event.type == KEYUP:
            if event.key == K_LCTRL or event.key == K_RCTRL:
                self.ctrlDown=False
        elif event.type == KEYDOWN:
            if event.key == K_LCTRL or event.key == K_RCTRL:
                self.ctrlDown=True
            #elif event.key==K_F1 or event.key==K_PAUSE or (self.ctrlDown and event.key==K_h):
            #    self.ctrlDown=False
            #    self.table.info.help.transient(self.screen)
            elif event.key==K_i:
                self.table.showHandsInfo(self.screen)
            elif event.key==K_b:
                self.table.bidding.historybox.transient(self.screen)
            #elif event.key==K_F5 or (event.key==K_n and self.ctrlDown):
            #    self.ctrlDown=False
            #    self.table.newHand(self.screen)
            elif event.key==K_F9:
                self.table.toggleShowAllHands(self.screen)
        return True



def main(scale=1.0):
    x,y,dx,dy=0,0,int(720*scale),int(540*scale)
    os.environ['SDL_VIDEO_WINDOW_POS']=str(x)+","+str(y)
    pygame.init()
    pygame.display.set_caption('Bridget')
    screen=pygame.display.set_mode((dx,dy))#HWSURFACE|RESIZABLE)
    g=Bridget(screen)
#    g.loop()
    pygame.quit()
if __name__ == '__main__': main()

