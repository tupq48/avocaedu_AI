class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        mySet = set()
        for line in nums:
            for number in range(line[0], line[1] + 1):
                mySet.add(number)
        return len(mySet)
