# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_val = 0
        nums_sum = 0
        temp_dict = {0: -1}
        for i, _num in enumerate(nums):
            if _num == 0:
                nums_sum -= 1
            else:
                nums_sum += 1
            
            if nums_sum in temp_dict:
                max_val = max(max_val, i - temp_dict[nums_sum])
            else:
                temp_dict[nums_sum] = i
        # print(temp_dict)
        return max_val

        # for i in range(len(nums), 0, -1):
        #     for n in range(len(nums)-i+1):
        #         _nums = nums[n:n+i]
        #         if (_nums.count(1) - _nums.count(0)) == 0:
        #             return i
        # return 0


if __name__ == "__main__":
    solution = Solution()
    answer = solution.findMaxLength([0,0,1,0,0,0,1,1])
    print(answer)

    # answer = solution.findMaxLength([0,1])
    # print(answer)
