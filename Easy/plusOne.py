class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        to_add = 1
        i = len(digits) - 1
        done = False
        while not done and i >= 0:
            d = (digits[i] + to_add) % 10
            if d != 0:
                digits[i] = d
                done = True
                break
            else:
                digits[i] = d
                i -= 1

        if not done:
            digits.insert(0, to_add)
        return digits
