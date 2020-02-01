from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = set()
        ind = {}

        for i, n in enumerate(nums):
            if n in search:
                return [ind[target - n], i]

            diff = target - n
            search.add(diff)
            ind[n] = i