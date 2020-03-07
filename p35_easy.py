# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    answer1 = solution.searchInsert([], 4)
    print(answer1)
    
    answer2 = solution.searchInsert([1,3,5,6], 7)
    print(answer2)
