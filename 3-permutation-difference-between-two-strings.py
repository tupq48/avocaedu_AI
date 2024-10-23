class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        i, j = 0, 0
        res = 0
        for c1 in s:
            j = 0
            for c2 in t:
                if (c2 == c1):
                    temp = j - i
                    res += temp if temp > 0 else temp*-1
                    break
                j += 1
            i += 1
        return res
