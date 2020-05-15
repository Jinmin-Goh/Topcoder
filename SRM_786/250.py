# Contest No.: 786
# Problem No.: 250
# Solver:      JEMINI
# Date:        20200515

class CutTheCube():
    def findWinner(self, L, B, H):
        if L * B * H == 1:
            return 2
        if (L * B * H - 1) % 2:
            return 1
        else:
            return 2