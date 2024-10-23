from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        selected = [False] * 10
        self.solve(turnedOn, selected, res, 0)
        return res

    def solve(self, turnedOn, selected, res, start):
        # Stop condition
        if turnedOn == 0:
            time = self.findTime(selected)
            if time:
                res.append(time)
            return

        # try turn on another led
        for i in range(start, len(selected)):
            if selected[i]:
                continue
            selected[i] = True
            self.solve(turnedOn - 1, selected, res, i + 1)  
            selected[i] = False  # rool back (try skip this one)

    def findTime(self, selected):
        hour = 0
        hour += 8 if selected[0] else 0
        hour += 4 if selected[1] else 0
        hour += 2 if selected[2] else 0
        hour += 1 if selected[3] else 0

        minute = 0
        minute += 32 if selected[4] else 0
        minute += 16 if selected[5] else 0
        minute += 8 if selected[6] else 0
        minute += 4 if selected[7] else 0
        minute += 2 if selected[8] else 0
        minute += 1 if selected[9] else 0

        if hour < 12 and minute < 60:
            return f"{hour}:{minute:02d}"
        return None
