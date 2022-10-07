from ast import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num = [[] for _ in range(numRows)]
        num[0] = [1]
        for i in range(1, numRows):
            num[i] = [1] + [0]*(i - 1) + [1]
        for i in range(2, numRows):
            for j in range(1, i):
                num[i][j] = num[i - 1][j - 1] + num[i - 1][j]
        return num