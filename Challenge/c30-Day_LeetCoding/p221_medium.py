# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row > 0:
            col = len(matrix[0])
            if col == 0:
                return 0
        else:
            return 0
        _temp = [[0] * (col+1) for _ in range(row+1)]
        
        max_num = 0
        for i in range(row):
            for j in range(col):
                if (matrix[i][j] == "1") or (matrix[i][j] == 1):
                    _temp[i+1][j+1] = min(_temp[i][j+1], _temp[i+1][j], _temp[i][j]) + 1
                    if _temp[i+1][j+1] > max_num:
                        max_num = _temp[i+1][j+1]
        return max_num**2


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    # matrix = [[]]
    answer = solution.maximalSquare(matrix)
    print(answer)
