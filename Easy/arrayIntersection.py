class Solution:
    # [1,2,3] [2,3,4]
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i1 = 0
        i2 = 0

        ans = []
        while i1 < len(nums1) and i2 < len(nums2):
            # print(nums1[i1], nums2[i2])
            if nums1[i1] == nums2[i2]:
                ans.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                # print("less")
                i1 += 1
            else:
                # print("greater")
                i2 += 1

        return ans
