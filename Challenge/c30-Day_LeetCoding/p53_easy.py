# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = sum_num = nums[0]
        for num in nums[1:]:
            if sum_num < 0:
                sum_num = num
            else:
                sum_num += num
            if sum_num > max_num:
                max_num = sum_num
        return max_num


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
