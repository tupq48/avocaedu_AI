class Solution:
    def checkString(self, s: str) -> bool:
        hasB = False
        for c in s:
            if c == 'a' and hasB:
                return False
            if c == 'b':
                hasB = True
        return True
