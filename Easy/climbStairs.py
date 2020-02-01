class Solution:
    def __init__(self):
        self.combis = {
            0: 1,
            1: 1,
            2: 2,
            3: 3,
        }

    def climbStairs(self, n: int) -> int:
        if self.combis.get(n) != None:
            return self.combis[n]

        for i in range(len(self.combis.items()), n + 1):
            current = self.combis[i - 1] + self.combis[i - 2]
            self.combis[i] = current

        return self.combis[n]