class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxVal = nums[0]
        for num in nums:
            if num > maxVal:
                maxVal = num
        return (maxVal+maxVal+k-1)*k//2
