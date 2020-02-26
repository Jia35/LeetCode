# 1. Two Sum
# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out1 = 0
        out2 = 0
        for index1, num1 in enumerate(nums):
            for index2 in range(index1+1, len(nums)):
                num2 = nums[index2]
                if num1 + num2 == target:
                    out1 = index1
                    out2 = index2
        return [out1, out2]


if __name__ == "__main__":
    solution = Solution()
    answer = solution.twoSum([2, 7, 11, 15], 9)
    print(answer)
