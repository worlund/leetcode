class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n-1.0 < 0.00000001:
            return True
        elif n < 1:
            return False
        else:
            print(n)
            return self.isPowerOfThree(n/3)