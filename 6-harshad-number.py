class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res = 0
        old_x = x
        while (x > 0):
            res += x % 10
            x = x // 10
        if (old_x % res == 0):
            return res
        return -1
