# Contest No.: 787
# Problem No.: 250
# Solver:      JEMINI
# Date:        20200622

class AqaAsadiNames():
    def getName(self, Dad, Mom, FirstChild, Gender):
        Dad = list(Dad.split())
        Mom = list(Mom.split())
        FirstChild = list(FirstChild.split())
        firstGender = "Boy"
        if FirstChild[0][0] in ["A", "E", "I", "O", "U", "Y"]:
            firstGender = "Girl"
        ans = ""
        if firstGender == Gender:
            if Gender == "Boy":
                ans = Dad[0] + " " + FirstChild[1]
            else:
                ans = Mom[0] + " " + FirstChild[1]
        else:
            if Gender == "Boy":
                ans = Dad[1] + " " + Dad[0]
            else:
                ans = Mom[1] + " " + Mom[0]
        return ans