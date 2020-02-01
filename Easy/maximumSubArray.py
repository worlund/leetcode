from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        partial = [0] * len(nums)
        partial[0] = nums[0]

        for i in range(1, len(nums)):
            partial[i] = max(partial[i - 1] + nums[i], nums[i])
        return max(partial)


test = Solution()
test_data = [1, 3, -2, -3, 1, -5, 5, 7, -2, 8]
print(test.maxSubArray(test_data))
print(test.maxSubArray(test_data[2:6]))
