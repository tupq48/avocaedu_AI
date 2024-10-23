class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
            return arr
        mVal = arr[-1]
        arr[-1] = -1  
        for i in range(len(arr) - 2, -1, -1):
            current = arr[i] 
            arr[i] = mVal  
            if current > mVal:
                mVal = current
        return arr
