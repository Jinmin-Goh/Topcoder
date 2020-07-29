# Contest No.: SRM788
# Problem No.: 300
# Solver:      JEMINI
# Date:        20200724

class NextOlympics():
    def countDays(self, today):
        year = int(today[:4])
        month = int(today[5:7])
        day = int(today[8:])

        ans = 0
        if year == 2020:
            ans += 204
            if month == 12:
                ans += 31 - day
            elif month == 11:
                ans += 31 + (30 - day)
            elif month == 10:
                ans += 61 + (31 - day)
            elif month == 9:
                ans += 92 + (30 - day)
            elif month == 8:
                ans += 122 + (31 - day)
            elif month == 7:
                ans += 153 + (31 - day)
            
        else:
            if month == 7:
                ans = 23 - day
            elif month == 6:
                ans = 23 + (30 - day)
            elif month == 5:
                ans = 53 + (31 - day)
            elif month == 4:
                ans = 84 + (30 - day)
            elif month == 3:
                ans = 114 + (31 - day)
            elif month == 2:
                ans = 145 + (28 - day)
            elif month == 1:
                ans = 173 + (31 - day)
        return ans