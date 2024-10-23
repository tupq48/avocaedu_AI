class Solution:
    def is_symmetric(self, num: int):
        s = str(num)
        n = len(s)
        if n % 2 != 0:
            return False
        half = n // 2
        first_half_sum = sum(int(s[i]) for i in range(half))
        second_half_sum = sum(int(s[i]) for i in range(half, n))
        return first_half_sum == second_half_sum

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if self.is_symmetric(num):
                count += 1
        return count
