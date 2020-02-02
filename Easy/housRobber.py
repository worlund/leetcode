from typing import List

def rob(nums: List[int]) -> int:
    dp = [0] * len(nums)
    if len(nums) < 3:
        return max(nums)

    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[0] + nums[2]
    maxRes = max(dp)
    for n in range(3, len(nums)):
        curr = nums[n]
        dp[n] = max(dp[n - 2]+curr, dp[n - 3]+curr)
        maxRes = max(maxRes, dp[n])

    return maxRes

test = [2,7,9,3,1]
print(rob(test))