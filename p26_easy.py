# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
        # tmp = ''
        # i = 0
        # while i < len(nums):
        #     num = nums[i]
        #     if num == tmp:
        #         nums.remove(num)
        #         i -= 1
        #     else:
        #         tmp = num
        #     i += 1
        # return nums


if __name__ == "__main__":
    solution = Solution()
    # input1 = [1,1,2]
    # answer1 = solution.removeDuplicates(input1)
    # print(answer1)

    # input2 = [0,0,1,1,1,2,2,3,3,4]
    # answer2 = solution.removeDuplicates(input2)
    # print(answer2)

    input3 = [-1,0,0,0,0,3,3]
    answer3 = solution.removeDuplicates(input3)
    print(answer3)
    