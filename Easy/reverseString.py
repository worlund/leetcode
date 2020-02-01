class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        start = 0
        end = len(s)//2
        last = len(s)-1
        for i in range(start, end):
            tmp = s[i]
            s[i] = s[last-i]
            s[last-i] = tmp
        '''
        i = 0
        for c in s[::-1]:
            s[i] = c
            i += 1
