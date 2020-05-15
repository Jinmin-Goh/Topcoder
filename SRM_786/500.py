# Contest No.: 786
# Problem No.: 500
# Solver:      JEMINI
# Date:        20200516

class SmallestRegular():
    def findLexSmallest(self, S):
        ans = []
        flag = False
        for i in range(len(S)):
            if S[i] == ")":
                flag = True
            else:
                if flag:
                    ans += [0, i - 1, i]

        return tuple(ans)