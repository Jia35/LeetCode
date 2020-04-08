# 136. Single Number
# https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == nums[i-1]:
                i -= 2
            else:
                return nums[i]


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([4,1,2,1,2]))
