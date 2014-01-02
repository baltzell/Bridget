from Globals import DECKDEFS
class Bid():
    def __init__(self,level,trump=None,owner=None):
        self.level=level
        self.owner=owner
        self.trump=None
        self.value=0
        self.double=0
        if trump==None:
            if self.level>0:
                self.double==self.level
        else:
            if type(trump) is str:
                self.trump=DECKDEFS.trumps1.index(trump[0].lower())
            else:
                self.trump=trump
            self.value=(self.level-1)*DECKDEFS.ntrumps+self.trump+1
        self.name=self.human()
    def human(self):
        if self.trump==None:
            if self.level==0:
                return 'pass'
            elif self.level==1:
                return '*'
            else:
                return '**'
        else:
            return str(self.level)+DECKDEFS.trumps[self.trump]
    def __eq__(self,bid):
        return self.value==bid.value
    def __ne__(self,bid):
        return not self.__eq__(bid)
    def __gt__(self,bid):
        return self.value>bid.value
    def __lt__(self,bid):
        return self.value<bid.value
    def __ge__(self,bid):
        return not self.__lt__(bid)
    def __le__(self,bid):
        return not self.__gt__(bid)

