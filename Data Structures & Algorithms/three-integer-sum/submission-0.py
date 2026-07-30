class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            # Only tracks elements less than 0.
            if a > 0: break

            # If duplicate, just skip, it's redundant.
            if i > 0 and a == nums[i - 1]: continue 

            # Set "l" next to i; put "r" at the end.
            l, r = i + 1, len(nums) - 1
            while l < r:
                # Check three sum value if it equals 0.
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # If it does, add it to the result.
                    result.append([a, nums[l], nums[r]])

                    # Increment to progress through the list.
                    l += 1
                    r -= 1

                    # This also prevents duplicate triplets.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result           