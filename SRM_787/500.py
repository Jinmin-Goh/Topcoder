# Contest No.: 787
# Problem No.: 500
# Solver:      JEMINI
# Date:        20200622

class AqaAsadiPlays():
    def getMin(self, A):
        def gcd(a, b):
            if a < b:
                a, b = b, a
            if b == 0:
                return a
            return gcd(b, a % b)
        

        if len(A) == 1:
            return -1
        if len(A) == 2:
            if A[0] == A[1]:
                return -1
            else:
                return 1
        
        A = list(A)
        A.sort()
        A = list(reversed(A))
        if A[0] == A[-1]:
            return -1
        curGCD = A[0]
        ans = 1
        for i in range(1, len(A) - 1):
            curGCD = gcd(curGCD, A[i])
            
            if curGCD > A[i + 1]:
                ans = i + 1
            #print(curGCD, i, A[i], A[i + 1], ans)
        return ans
