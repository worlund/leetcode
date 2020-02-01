class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        tSum = 0
        iSum = 0
        for i in range(n):
            tSum += (i + 1)
            iSum += nums[i]

        return tSum - iSum