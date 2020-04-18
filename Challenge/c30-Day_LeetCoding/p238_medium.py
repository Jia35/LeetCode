# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_nums = [1]
        l_nums = [1]
        for i in range(len(nums)-1):
            l_nums.append(nums[i] * l_nums[i])
        
        for i in range(len(nums)-1, 0, -1):
            r_nums.insert(0, nums[i] * r_nums[0])

        return [l*r for l, r in zip(l_nums, r_nums)]

        # ans = [1 for _ in nums]
        # left = 1
        # right = 1
        
        # for i in range(len(nums)):
        #     ans[i] *= left
        #     ans[-1-i] *= right
        #     left *= nums[i]
        #     right *= nums[-1-i]
        # return ans
        
        # out_nums = []
        # for i in range(len(nums)):
        #     _temp = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             _temp *= nums[j]
            
        #     out_nums.append(_temp)
        # return out_nums


if __name__ == "__main__":
    solution = Solution()
    answer = solution.productExceptSelf([4,5,1,8,2])
    print(answer)
