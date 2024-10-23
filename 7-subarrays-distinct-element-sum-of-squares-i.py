class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)):
            mySet = set()
            for j in range(i, len(nums)):
               mySet.add(nums[j])
               res += len(mySet)*len(mySet)

        return res 
