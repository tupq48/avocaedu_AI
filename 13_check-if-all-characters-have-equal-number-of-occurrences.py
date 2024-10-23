class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        myDict = {}
        for c in s:
            if c not in myDict:
                myDict[c] = 1
            else:
                myDict[c] += 1  

        val = myDict[s[0]]  
        for k, v in myDict.items():
            if v != val:  
                return False
        return True
