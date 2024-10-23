class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x//2+1
        // binary search
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return int(mid)
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return int(right)
