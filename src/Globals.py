import pygame
from Utilities import Utilities
class Beeps():
    def __init__(self):
        for ii in (1,2,3,4):
            self.beeps[ii]=pygame.mixer.Sound("./snd/beep%d.ogg" % ii)
class Fonts():
    def __init__(self):
        self.fonttype='fixed'
        self.fonts={}
        pygame.font.init()
        for fontsize in (10,12,13,14,15,16,18,20,24,28,32,80):
            self.fonts[fontsize]=pygame.font.SysFont(self.fonttype,fontsize)
class Colors():
    def __init__(self):
        self.colors={'table'       : (0x00,0x50,0x00),
#                     'tablelight'  : (0x50,0xb0,0x00),
                     'tablelight'  : (0x00,0x60,0x00),
                     'tabledark'   : (0x00,0x40,0x00),
                     'lightred'    : (0xe0,0xa0,0x40),
                     'white'       : (0xff,0xff,0xff),
                     'black'       : (0x00,0x00,0x00),
                     'darkyellow'  : (0xbb,0xbb,0x00),
                     'grey'        : (0x66,0x66,0x66),
                     'yellow'      : pygame.Color('yellow'),
                     'red'         : pygame.Color('red'),
                     '0'           : pygame.Color('magenta'),
                     '1'           : pygame.Color('blue'),
                     '2'           : pygame.Color('yellow'),
                     '3'           : pygame.Color('green')}
class DeckDefs():
    def __init__(self):
        self.ranks=['2','3','4','5','6','7','8','9','Ten','Jack','Queen','King','Ace']
        self.seats=['North','East','South','West']
        self.suits=['Clubs','Diamonds','Hearts','Spades']
        self.trumps=['Clubs','Diamonds','Hearts','Spades','NT']
        self.nsuits=len(self.suits)
        self.nranks=len(self.ranks)
        self.nseats=len(self.seats)
        self.ntrumps=len(self.trumps)
        self.ncards=self.nsuits*self.nranks
        self.backimage=pygame.image.load("../gifs/b.gif")
        self.cardsize=self.backimage.get_rect().size
        self.images,self.smallimages,self.ranks1,self.suits1,self.seats1=[],[],[],[],[]
        for suit in self.suits:
            for rank in self.ranks:
                giffile="../gifs/%s%s.gif" % (rank[0].lower(),suit[0].lower())
                self.images.append(pygame.image.load(giffile))
                giffile="../gifs/small_%s%s.gif" % (rank[0].lower(),suit[0].lower())
                self.smallimages.append(pygame.image.load(giffile))
        for suit in self.suits: self.images.append(pygame.image.load("../gifs/"+suit[0].lower()+".gif"))
        for suit in self.suits: self.images.append(pygame.image.load("../gifs/"+suit[0].lower()+"_green.gif"))
        self.ranks1 =[x[0].lower() for x in self.ranks]
        self.suits1 =[x[0].lower() for x in self.suits]
        self.seats1 =[x[0].lower() for x in self.seats]
        self.trumps1=[x[0].lower() for x in self.trumps]

#BEEPS=Beeps().beeps
DECKDEFS=DeckDefs()
FONTS=Fonts().fonts
COLORS=Colors().colors
UTILITIES=Utilities(DECKDEFS,COLORS,FONTS)

