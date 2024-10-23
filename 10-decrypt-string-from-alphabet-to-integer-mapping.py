class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == '#':
                # get 2 digit
                temp = int(s[i:i+2])  
                res += chr(temp + 96)  # 'a' start 97 in ascii
                i += 3  # skip '#'
            else:
                temp = int(s[i])
                res += chr(temp + 96)  # 'a' start 97 in ascii
                i += 1
        return res
