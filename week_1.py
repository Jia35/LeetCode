# 2020/04 舉辦的30天挑戰
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/

# Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Happy Number
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.

# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

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

    def isHappy(self, n: int) -> bool:
        _temp_list = []
        while n != 1:
            n = sum([int(s) ** 2 for s in str(n)])
            if n in _temp_list:
                return False
            _temp_list.append(n)
        return True

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

    def moveZeroes(self, nums: List[int]) -> None:
        n = 0
        for m in range(len(nums)):
            if nums[m] != 0:
                nums[n], nums[m] = nums[m], nums[n]
                n += 1


if __name__ == "__main__":
    solution = Solution()

    print(solution.singleNumber([4,1,2,1,2]))

    print(solution.isHappy(19))

    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    
    input_list = [0,1,0,3,12]
    solution.moveZeroes(input_list)
    print(input_list)
