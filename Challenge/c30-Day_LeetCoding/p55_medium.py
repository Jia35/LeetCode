# 55. Jump Game
# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def find_zero(nums, start):
            for index, num in enumerate(nums[start:]):
                if num == 0:
                    return start + index
            return -1
        
        if len(nums) <= 1:
            return True
        nums = nums[:-1]
        start_index = 0
        while 1:
            step = 1
            index = find_zero(nums, start_index)
            if index == -1:
                break
            
            start_index = index + 1
            is_ok = False
            while index > 0:
                index -= 1
                if nums[index] > step:
                    is_ok = True
                    break
                step += 1
            
            if not is_ok:
                return False
        return True
        # nums_len = len(nums)
        # if nums_len <= 1:
        #     return True
        
        # _temp = [0 for _ in range(nums_len)]

        # for index, num in enumerate(nums[:-1]):
        #     index_end = index + num
        #     if index_end > nums_len:
        #         index_end = nums_len
            
        #     for n in range(index, index_end):
        #         if _temp[n] == 0:
        #             _temp[n] = 1
        
        # return (0 not in _temp[:-1])


if __name__ == "__main__":
    solution = Solution()
    # in_list = [2,3,1,1,4]
    # in_list = [3,2,1,0,4]
    in_list = [2,0,0]
    answer = solution.canJump(in_list)
    print(answer)
