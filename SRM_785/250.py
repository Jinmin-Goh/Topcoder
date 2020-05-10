# Contest No.: 785
# Problem No.: 250
# Solver:      JEMINI
# Date:        20200510

import sys

class EllysPalMulDiv2():
    def getMin(self, X):
        self.ans = -1
        for i in range(1, 1001):
            temp = str(X * i)
            flag = True
            for j in range(len(temp) // 2):
                if temp[j] != temp[-j - 1]:
                    flag = False
                    break
            if flag:
                self.ans = i
                break
        return self.ans
        