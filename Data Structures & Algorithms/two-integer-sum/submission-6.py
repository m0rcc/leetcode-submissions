class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement, difference = {}, 0

        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in complement:
                return [complement[nums[i]], i]
            
            complement[difference] = i
            