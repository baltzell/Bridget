class TeamScore():
    def __init__(self):
        self.over=0
        self.under=[0]
class Score():
    def __init__(self):
        self.games=[0,0]
        self.scores=(TeamScore(),TeamScore())
    def addScore(self,contract,trickcount):
        over,under=0,0
        difference=trickcount[contract.owner%2]-(contract.level+6)

        if difference<0:
            self.scores[(contract.owner+1)%2].over -= 50*difference

        else:
            # contract value:
            if contract.trump<2: #minor
                under=20*contract.level
            elif contract.trump<4: #major
                under=30*contract.level
            else: #notrump
                under=40+30*(contract.level-1)
            if contract.level==6: #small slam
                under+=200
            elif contract.level==7: #grand slam
                under+=500
            # overtricks:
            if difference>0:
                if contract.trump<2:
                    over=20*difference
                else:
                    over=30*difference
            # set score:
            iteam=contract.owner%2
            igame=len(self.scores[iteam].under)-1
            self.scores[iteam].under[igame] += under
            self.scores[iteam].over         += over
            if self.scores[iteam].under[igame]>=100:
                self.games[iteam]+=1
                if self.games[iteam]<2:
                    self.scores[iteam].under.append(0)
                    self.scores[(iteam+1)%2].under.append(0)
                else:
                    # rubber is over:
                    return False

        return True
