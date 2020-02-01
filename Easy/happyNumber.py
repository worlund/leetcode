class Solution:
    def __init__(self):
        self.happys = set([1])

    def isHappy(self, n: int) -> bool:
        if n in self.happys:
            return True

        numbers = set([n])

        def calcSum(z: int) -> int:
            s = 0
            while z > 0:
                s += (z % 10) ** 2
                z = z // 10
            return s

        print(n)
        i = 0
        while i < 10:
            partialsum = calcSum(n)
            print(partialsum)
            n = partialsum
            numbers.add(partialsum)
            if partialsum in self.happys:
                self.happys.union(numbers)
                return True
            i += 1
        return False
