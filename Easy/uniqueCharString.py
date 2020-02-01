class Solution:
    def firstUniqChar(self, s: str) -> int:
        occur = {}

        for c in s:
            occur[c] = 1 if occur.get(c) == None else occur[c] + 1

        for i, c in enumerate(s):
            if occur[c] == 1:
                return i
        return -1