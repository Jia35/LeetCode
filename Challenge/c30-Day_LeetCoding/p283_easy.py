# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = 0
        for m in range(len(nums)):
            if nums[m] != 0:
                nums[n], nums[m] = nums[m], nums[n]
                n += 1


if __name__ == "__main__":
    solution = Solution()
    input_list = [0,1,0,3,12]
    solution.moveZeroes(input_list)
    print(input_list)
