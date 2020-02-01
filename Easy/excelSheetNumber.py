class Solution:
    def __init__(self):
        self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphsize = len(self.alph)
        self.alphaDict = {}
        i = 1
        for c in self.alph:
            self.alphaDict[c] = i
            i += 1

    def titleToNumber(self, s: str) -> int:
        if len(s) == 1:
            return self.alphaDict[s]
        else:
            res = 0
            chars = len(s)
            offset = 0
            for c in s[::-1]:
                res += self.alphaDict[c] * pow(self.alphsize, offset)
                offset += 1
            return res