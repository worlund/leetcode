class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        alternatively just put them in and then use .sort
        """
        tmp = [0] * (m + n)
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            n1 = nums1[i]
            n2 = nums2[j]

            if n1 < n2:
                tmp[k] = n1
                i += 1
            elif n2 < n1:
                tmp[k] = n2
                j += 1
            else:
                tmp[k] = n1
                tmp[k + 1] = n2
                k += 1
                i += 1
                j += 1
            k += 1

        while i < m:
            tmp[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            tmp[k] = nums2[j]
            j += 1
            k += 1

        for w in range(m + n):
            nums1[w] = tmp[w]
