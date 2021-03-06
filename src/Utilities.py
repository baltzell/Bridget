import pygame,sys
from pygame import locals
class Utilities():
    def __init__(self,deck,colors,fonts):
        self.deck=deck
        self.colors=colors
        self.fonts=fonts
    def image(self,sorhori,rank=None):
        return self.deck.images[self.index(sorhori,rank)]
    def smallimage(self,sorhori,rank=None):
        return self.deck.smallimages[self.index(sorhori,rank)]
    def name(self,index):
        return self.rank(index)+self.suit(index)
    def isuit(self,index):
        return index/len(self.deck.ranks)
    def irank(self,index):
        return index%len(self.deck.ranks)
    def suit(self,index):
        return self.deck.suits[self.isuit(index)]
    def rank(self,index):
        return self.deck.ranks[self.irank(index)]
    def color(self,index):
        return ('black','red')[index/len(self.deck.ranks)%2]
    def index(self,sorhori,rank=None):
        if rank:
            return sorhori*len(self.deck.ranks)+rank
        elif type(sorhori) is int:
            return sorhori
        else:
            suit,rank=-1,-1
            for ii in range(len(self.deck.suits)):
                if self.deck.suits[ii].lower() == sorhori[1].lower():
                    suit=ii
                    break
            for ii in range(len(self.deck.ranks)):
                if deck.ranks[ii].lower() == sorhori[0].lower():
                    rank=ii
                    break
            return suit*len(self.deck.ranks)+rank
    def globalShortcuts(self,event,ctrldown):
        pygl=pygame.locals
        if event.type==pygl.VIDEORESIZE:
            pygame.display.set_mode(event.size,pygl.RESIZABLE)
            pygame.display.flip()
            return True
        elif event.type==pygl.QUIT:
            self.quit()
        elif event.type==pygl.KEYUP and ctrldown:
            if (event.key==pygl.K_q or event.key==pygl.K_c or event.key==pygl.K_ESCAPE):
                self.quit()
            elif event.key==pygl.K_f:
                pygame.display.toggle_fullscreen()
                return True
            elif event.key==pygl.K_h:
                # transient help screen
                pass
        return False
    def pause(self):
        while 1:
            event=pygame.event.wait()
            if event.type==pygame.locals.KEYDOWN:
                break
            if event.type==pygame.locals.MOUSEBUTTONDOWN:
                break
        pygame.event.clear()
    def quit(self):
        pygame.quit()
        sys.exit()
    def pressAnyKey(self,screen):
        oldsurf=screen.copy()
        font=self.fonts[18]
        img=font.render('Press any key ....',1,self.colors['yellow'])
        rect=img.get_rect()
        rect.centerx=screen.get_rect().centerx
        rect.top=self.deck.cardsize[1]+30
        screen.blit(img,rect.topleft)
        pygame.display.flip()
        self.pause()
        screen.blit(oldsurf,(0,0))
        pygame.display.flip()
    def sortValue(self,index):
        return (2,3,1,0)[self.deck.isuit(index)]*range(12,-1,-1)[self.deck.irank(index)]
    def sortCards(self,cards):
        newcards=[]
        for suit in (3,2,0,1):
            for rank in range(12,-1,-1):
                index=suit*self.deck.nranks+rank
                for card in cards:
                    if card==index:
                        newcards.append(card)
                        break
        return newcards
    def blitBid(self,font,surf,bid,colorfg,pos,greenback=False):
        if bid.trump==None:
            img=font.render(bid.name,1,colorfg)
            self.blitImg(surf,img,pos)
        else:
            if bid.trump<self.deck.ntrumps-1:
                img1=font.render(str(bid.level),1,colorfg)
                if greenback:
                    img2=self.deck.images[self.deck.ncards+bid.trump+4]
                else:
                    img2=self.deck.images[self.deck.ncards+bid.trump]
                self.blitImgs(surf,img1,img2,pos)
            else:
                img=font.render(bid.name,1,colorfg)
                self.blitImg(surf,img,pos)
    def blitImgs(self,surf,img1,img2,pos):
        img1rect=img1.get_rect()
        img1rect.centerx=pos[0]-img1rect.width/2-2-5
        img1rect.centery=pos[1]
        surf.blit(img1,img1rect.topleft)
        img2rect=img2.get_rect()
        img2rect.centerx=pos[0]+img2rect.width/2+2-5
        img2rect.centery=pos[1]
        surf.blit(img2,img2rect.topleft)
    def blitImg(self,surf,img,pos):
        imgrect=img.get_rect()
        imgrect.centerx,imgrect.centery=pos[0],pos[1]
        surf.blit(img,imgrect.topleft)
    def drawHorLine(self,surf,y,color,offset=0):
        start,end=(offset,y),(surf.get_rect().width-offset,y)
        pygame.draw.line(surf,color,start,end,1)
    def drawVerLine(self,surf,x,color,offset=0):
        start,end=(x,offset),(x,surf.get_rect().height-offset)
        pygame.draw.line(surf,color,start,end,1)
    def arrowHeadPoints(self,surf,direction):
        off=1
        (dx,dy)=surf.get_rect().size
        if direction=='u':
            points=((off,off),(dx/2,dy-off),(dx-off,off))
        elif direction=='d':
            points=((off,dy),(dx/2,off),(dx-off,dy-off))
        elif direction=='l':
            points=((off,off),(dx-off,dy/2),(off,dy-off))
        elif direction=='r':
            points=((dx-off,off),(off,dy/2),(dx-off,dy-off))
        return points
    def drawArrowHead(self,surf,color,direction):
        points=self.arrowHeadPoints(surf,direction)
        pygame.draw.polygon(surf,color,points)

