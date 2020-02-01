class Solution:
    '''
        iterate over numbers 1 to n
        check if number is a multiple of 3 and 5 append Fizz and Buzz respectively
        else append number as a string
    '''

    def fizzBuzz(self, n: int) -> List[str]:
        res = [""] * n
        for i in range(n):

            if (i + 1) % 3 == 0:
                res[i] += "Fizz"
            if (i + 1) % 5 == 0:
                res[i] += "Buzz"

            if res[i] == "":
                res[i] = str(i + 1)
        return res