class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        digits = self.countAndSay(n-1)
        prev = digits[0]
        amount = 1
        next = ""
        for c in digits[1:]:
            if c != prev:
                next += str(amount) + str(prev)
                prev = c
                amount = 1
            else:
                amount += 1
        next += str(amount) + str(prev)
        return next


#input = 1
#input2 = 2
#input3 = 6
#test = Solution()

#print(input, test.countAndSay(input))
#print(input2, (test.countAndSay(input2)))
#print(input3, (test.countAndSay(input3)))