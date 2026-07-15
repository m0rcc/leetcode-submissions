class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement, difference = {}, 0

        for index in range(len(nums)):
            difference = target - nums[index]

            if nums[index] in complement:
                return [complement[nums[index]], index]
            
            complement[difference] = index
            