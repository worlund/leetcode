class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement1(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n // 2

        m_e = 0
        occurrences = {}

        for e in nums:
            if occurrences.get(e) is None:
                occurrences[e] = 1
            else:
                occurrences[e] += 1

            if occurrences[e] > majority:
                m_e = e
                return m_e

        return m_e

