'''
Remove duplicates in array
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                nums.remove(nums[i])
                i -= 1
            else:
                prev = nums[i]
            i += 1
        return len(nums)
