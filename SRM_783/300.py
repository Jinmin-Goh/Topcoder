# Contest No.: SRM783
# Problem No.: 300
# Solver:      JEMINI
# Date:        20200724

class PosNegDice():
    def evaluateRoll(self, T, positiveDice, negativeDice):
        posDiceSet = set(positiveDice)
        negDiceSet = set(negativeDice)
        
        posDiceDict = {}            
        for i in positiveDice:
            if i in posDiceDict:
                posDiceDict[i] += 1
            else:
                posDiceDict[i] = 1
        negDiceDict = {}    
        for i in negativeDice:
            if i in negDiceDict:
                negDiceDict[i] += 1
            else:
                negDiceDict[i] = 1
        
        dup = list(posDiceSet & negDiceSet)
        flag = 0
        for i in dup:
            if posDiceDict[i] == negDiceDict[i]:
                del posDiceDict[i]
                del negDiceDict[i]
            elif posDiceDict[i] > negDiceDict[i]:
                posDiceDict[i] -= negDiceDict[i]
                del negDiceDict[i]
            else:
                negDiceDict[i] -= posDiceDict[i]
                del posDiceDict[i]
        
        for i in posDiceDict:
            if i <= T:
                flag = 1
                break
        
        sumVal = 0
        for i in negDiceDict:
            sumVal += negDiceDict[i]
        ans = tuple([flag, sumVal])
        print(ans)
        return ans