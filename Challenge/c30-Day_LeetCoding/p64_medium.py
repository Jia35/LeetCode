# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def min_path(i, j, h, w):
            if _temp[i][j] > 0:
                return _temp[i][j]
            if (i == (h - 1)) and (j == (w - 1)):
                distance = 0
            elif i == (h - 1):
                distance = min_path(i, j+1, h, w)
            elif j == (w - 1):
                distance = min_path(i+1, j, h, w)
            else:
                r_sum = min_path(i, j+1, h, w)
                d_sum = min_path(i+1, j, h, w)
                distance = min(r_sum, d_sum)
            _temp[i][j] = grid[i][j] + distance
            return grid[i][j] + distance
        
        h = len(grid)
        if h > 0:
            if len(grid[0]) != 0:
                w = len(grid[0])
                _temp = [[0]*w for _ in range(h)]
            else:
                return 0
        else:
            return 0
        return min_path(0, 0, h, w)

        # if len(grid) <= 0 or grid is None:
        #     return 0
        
        # rows = len(grid)
        # cols = len(grid[0])
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r == 0) and (c == 0):  # We just want to skip the top-left corner of the grid
        #             continue
        #         if (r - 1) < 0:  # Cases for elements in top row
        #             grid[r][c] = grid[r][c] + grid[r][c-1]  
        #         elif (c - 1) < 0:   # Cases for elements in leftmost column
        #             grid[r][c] = grid[r][c] + grid[r-1][c]  
        #         else:  # Normal cell
        #             grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])               
        
        # return grid[rows-1][cols-1]


if __name__ == "__main__":
    solution = Solution()
    map_island = [[1,3,1],
                  [1,5,1],
                  [4,2,1]]
    answer = solution.minPathSum(map_island)
    print(answer)
