class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = None
        b = None
        myS = set()
        sum = 0
        for row in grid:
            for col in row:
                sum += col
                if col in myS:
                    a = col
                    continue
                myS.add(col)
        n = len(grid[0])
        n = n*n
        b = n*(n+1)//2 - sum + a
        return [a,b]
