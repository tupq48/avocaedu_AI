class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a1 = ord(coordinate1[0]) - ord('a')
        a2 = int(coordinate1[1])
        b1 = ord(coordinate2[0]) - ord('a')
        b2 = int(coordinate2[1])
        first = (a1 + a2) % 2 == 0
        second = (b1 + b2) % 2 == 0
        return first == second
