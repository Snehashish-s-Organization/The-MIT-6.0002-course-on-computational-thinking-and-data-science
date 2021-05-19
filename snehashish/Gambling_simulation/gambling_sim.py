"""
implements the idea of a roulette game
"""

import random


# defining the roulette class which will simulate the roulette wheel
class rouletteSim():
    """
    defining a __init__ method that constructs the wheel
    the list pockets is bassically the pockets on the wheel
    and th profit earned with a None ball are defined
    """
 
    def __init__(self):

        self.pockets = []

        for i in range(1, 37):
            self.pockets.append(i)

        self.ball = None
        self.profit = len(self.pockets)-1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def bet(self, mypocket, amount):
        if str(mypocket) == str(self.ball):
            return amount*self.profit

        else:
            return -amount

    def __str__(self):
        return 'a fair roulette game'
        

def play(game, spins, pocket, amnt, printresults = True):
    totPocket = 0

    for i in range(spins):
        game.spin()
        totPocket += game.bet(pocket, amnt)

    if printresults:
        print(spins, 'spins of', game)
        print('Expected return betting', pocket, '=',str(100*totPocket/spins) + '%\n')
random.seed(0)
game = rouletteSim()
for spin in (10):
    print('\n---\n')
    pocket_to_gamble = random.randint(1, 37)
    for i in range(2):
        print(pocket_to_gamble)
        play(game, spin, pocket_to_gamble, 1)

class EuRoulette(rouletteSim):
    def __init__(self):
        rouletteSim.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'
        
def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = play(game, trialSize, 2, 1, toPrint)
        pocketReturns.append(trialVals)
    return pocketReturns

random.seed(0)
numTrials = 20
resultDict = {}
games = (rouletteSim, EuRoulette, AmRoulette)
for G in games:
    resultDict[G().__str__()] = []
for numSpins in (1000, 10000, 100000, 1000000):
    print('\nSimulate', numTrials, 'trials of',
          numSpins, 'spins each')
    for G in games:
        pocketReturns = findPocketReturn(G(), numTrials,
                                         numSpins, False)
        expReturn = 100*sum(pocketReturns)/len(pocketReturns)
        print('Exp. return for', G(), '=',
             str(round(expReturn, 4)) + '%')
             
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
