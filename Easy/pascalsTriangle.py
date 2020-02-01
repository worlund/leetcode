class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        if numRows < 2:
            return triangle[:numRows]

        return self.find_triangle(triangle, numRows)

    def find_triangle(self, triangle, numRows):
        res = triangle
        while len(res) < numRows:
            res.append(self.next_row(triangle[-1]))
        return res

    def next_row(self, prevRow):
        new_len = len(prevRow) + 1
        row = [1] * new_len

        for i in range(1, new_len - 1):
            row[i] = prevRow[i - 1] + prevRow[i]
        return row