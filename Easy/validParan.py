class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        left = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        open_p = []
        for c in s:
            if left.get(c):
                open_p.append(left[c])
            else:
                last = open_p[-1] if open_p else ""
                if c == last:
                    del open_p[-1]
                else:
                    return False

        if open_p:
            return False

        return True
