class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        prev = ""
        for char in s:
            if (char == "X" or char == "V") and prev == "I":
                res -= romans[prev] * 2
            if (char == "L" or char == "C") and prev == "X":
                res -= romans[prev] * 2
            if (char == "D" or char == "M") and prev == "C":
                res -= romans[prev] * 2
            res += romans[char]
            prev = char
        return res