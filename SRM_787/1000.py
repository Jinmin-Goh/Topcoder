# Contest No.: 787
# Problem No.: 1000
# Solver:      JEMINI
# Date:        20200622
import sys

class AqaAsadiGroups():
    def minimumDifference(self, Skills, k):
        n = len(Skills)
        sumVal = sum(Skills)
        # dpTable[i][j]: smallest possible unbalance ratio first i students j groups
        dpTable = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, k + 1):
            dpTable[0][i] = i * (sumVal ** 2)
        
        for i in range(n):
            for j in range(1, k + 1):
                curSum = 0
                dpTable[i + 1][j] = sys.maxsize
                for p in range(i, -1, -1):
                    curSum += Skills[p]
                    if j > 1 or p == 0:
                        dpTable[i + 1][j] = min(dpTable[i + 1][j], dpTable[p][j - 1] + (curSum * k - sumVal) ** 2)
        
        return dpTable[-1][-1]
        
        # WA code
        #cnt = 0
        #curSum = 0
        #ans = 0
        #for i in range(len(Skills)):
        #    if curSum == 0:
        #        curSum += Skills[i]
        #    else:
        #        if (curSum + Skills[i]) * k < sumVal:
        #            curSum += Skills[i]
        #        elif (curSum + Skills[i]) * k - sumVal < sumVal - curSum * k:
        #            curSum += Skills[i]
        #            ans += (curSum * k - sumVal) ** 2
        #            cnt += 1
        #            curSum = 0
        #        else:
        #            ans += (curSum * k - sumVal) ** 2
        #            cnt += 1
        #            curSum = Skills[i]
        #if cnt < k:
        #    while cnt < k:
        #        if curSum != 0:
        #            ans += (curSum * k - sumVal) ** 2
        #            cnt += 1
        #            curSum = 0
        #        else:
        #            ans += sumVal ** 2
        #            cnt += 1
#
        #return ans