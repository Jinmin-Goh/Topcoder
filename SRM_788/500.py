# Contest No.: SRM788
# Problem No.: 500
# Solver:      JEMINI
# Date:        20200724

class StarsInTheSky():
    def countPictures(self, N, X, Y):
        starX = []
        starY = []
        for i in range(N):
            starX.append((X[i], Y[i], i))
            starY.append((Y[i], X[i], i))
        starX.sort()
        starY.sort()
        
        setX = list(set(X))
        setY = list(set(Y))
        setX.sort()        
        setY.sort()
        ansSet = set()
        for xl in range(len(setX)):
            for xr in range(xl + 1, len(setX) + 1):
                for yl in range(len(setY)):
                    for yr in range(yl + 1, len(setY) + 1):
                        tempSetX = set()
                        tempSetY = set()
                        for x in starX:
                            if setX[xl] <= x[0] <= setX[xr - 1]:
                                tempSetX.add(x[2])
                        for y in starY:
                            if setY[yl] <= y[0] <= setY[yr - 1]:
                                tempSetY.add(y[2])
                        intersect = list(tempSetX & tempSetY)
                        if not intersect:
                            continue
                        intersect.sort()
                        intersect = tuple(intersect)
                        ansSet.add(intersect)
        return len(ansSet)