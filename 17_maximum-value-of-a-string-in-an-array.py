class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            try:
                val = int(s)
                if res < val:
                    res = val
            except:
                if res < len(s):
                    res = len(s)
        return res
