import random
from Bid import Bid
from Globals import DECKDEFS
def chooseBid(rubber):
    bidding=rubber.bidding
    nextseatind=bidding.nextSeatInd()
    hand=rubber.getHand(nextseatind)
    alreadypassed=False
    alreadybid=False
    partnerpassed=False
    partnerbid=False
    opponentsbid=False
    bid=None
    # OPENING BID
    if bidding.imaxbid<0:
        if hand.HCP>14 and hand.HCP<19 and hand.DP<2:
            bid=Bid(1,'NT')
        elif (hand.HCP+hand.DP)>21:
            bid=openingSuitBid(rubber)
        elif hand.HCP>11 or (hand.HCP+hand.DP)>13:
            bid=openingSuitBid(rubber)
    # RESPONSE BID
#    else:
#        if hand.HCP>12
    if not bid:
        bid=Bid(0)
    return bid

def openingSuitBid(rubber):
    iseat=rubber.bidding.nextSeatInd()
    hand=rubber.getHand(iseat)
    suits=hand.Suits()
    nmax,maxlen,lengths=0,0,[0,0,0,0]
    for isuit in range(len(suits)):
        lengths[isuit]=len(suits[isuit])
        if lengths[isuit]>=maxlen:
            nmax+=1
            if lengths[isuit]>maxlen:
                nmax=1
                maxlen=lengths[isuit]
    if maxlen>4:
        # at least one 5 card suit
        if nmax==1:  
            # only one longest suit:  pick it
            for isuit in range(len(lengths)):
                if maxlen==lengths[isuit]:
                    return Bid(1,isuit)
        else: 
            # multiple longest suits:  pick highest rank
            lengths.reverse()
            for isuit in range(len(lengths)):
                if lengths[isuit]==maxlen:
                    return Bid(1,(DECKDEFS.nsuits-isuit))
    else: 
        # no 5 card suit:  pick longer minor (diamonds if same length)
        if len(suits[0])>len(suits[1]):
            return Bid(1,0)
        else:
            return Bid(1,1)

def chooseCard(rubber):
    hand=rubber.getNextSeat()
    partnerhand=rubber.getPartner(hand)
    trick=rubber.currentTrick()

    # LEAD
    if not trick:
        return random.choice(hand.cards)
    if len(trick.cards)==0:
        return random.choice(hand.cards)

    trump=trick.trump
    isuit=trick.cards[0].isuit
    suit=hand.Suit(isuit)
    trumps=hand.Suit(trump)
    card=None

    if len(suit)==0 and len(trumps)>0:
        if hand.CanBeat(trick):
            if len(trumps)==1:
                card=trumps[0]
            else:
                card=hand.JustHighEnough(trick)#trumps[len(trumps)-1]

    elif len(suit)==1:             # only one legal play, play it
        card=suit[0]

    elif not hand.CanBeat(trick):  # impossible to win the trick, play low
        print 'cant beat, play low'
        card=hand.SuitLow(isuit)

    elif len(trick.cards)==1:      # second hand
        print 'second hand: low duck'
        card=hand.SuitLow(isuit)

    elif len(trick.cards)==2:      # third hand
        print 'third hand: high'
        card=hand.SuitHigh(isuit)

    elif len(trick.cards)==3:      # fourth hand
        print 'fourth hand: just high enough'
        card=hand.JustHighEnough(trick)

    if not card:  card=random.choice(hand.cards)

    return card

#class State():
#    def __init__(self,hand):
#        self.finesse=False

