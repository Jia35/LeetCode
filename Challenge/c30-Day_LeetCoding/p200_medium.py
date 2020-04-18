# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def set_island(grid, h, w, i, j):
            if i < (h - 1):
                if grid[i+1][j] == '1':
                    grid[i+1][j] = '2'
                    set_island(grid, h, w, i+1, j)
            if i > 0:
                if grid[i-1][j] == '1':
                    grid[i-1][j] = '2'
                    set_island(grid, h, w, i-1, j)
            if j < (w - 1):
                if grid[i][j+1] == '1':
                    grid[i][j+1] = '2'
                    set_island(grid, h, w, i, j+1)
            if j > 0:
                if grid[i][j-1] == '1':
                    grid[i][j-1] = '2'
                    set_island(grid, h, w, i, j-1)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    island_count += 1
                    set_island(grid, len(grid), len(grid[i]), i, j)
        return island_count


if __name__ == "__main__":
    solution = Solution()
    map_island = [["1","1","1","1","0"],
                  ["1","1","0","1","0"],
                  ["1","1","0","0","0"],
                  ["0","0","0","0","0"]]
    map_island = [["1","1","0","0","0"],
                  ["1","1","0","0","0"],
                  ["0","0","1","0","0"],
                  ["0","0","0","1","1"]]
    answer = solution.numIslands(map_island)
    print(answer)
