class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        size = len(arr)
        result = [0] * size
        rMax = -1

        for i in range(size - 1, -1, -1):
            result[i] = rMax
            rMax = max(arr[i], rMax)
        
        return result
        