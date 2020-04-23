# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            out = nums.index(target)
        except:
            out = -1
        return out


if __name__ == "__main__":
    solution = Solution()
    answer = solution.search([4,5,6,7,0,1,2], 0)
    print(answer)
