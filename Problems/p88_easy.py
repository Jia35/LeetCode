# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
from typing import List
import time

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num = 0
        i = 0
        j = 0
        while num != m:
            if j == n:
                break
            if nums1[i] > nums2[j]:
                nums1.insert(i, 0)
                nums1.pop()
                nums1[i] = nums2[j]
                j += 1
                num -= 1
            i += 1
            num += 1

        for _ in range(n-j):
            nums1.insert(i, 0)
            nums1.pop()
            nums1[i] = nums2[j]
            i += 1
            j += 1
        return nums1


if __name__ == "__main__":
    solution = Solution()
    # answer1 = solution.merge([1,2,3,4,0,0,0], 4, [2,5,6], 3)
    # print(answer1)
    
    # answer2 = solution.merge([], 0, [], 0)
    # print(answer2)

    answer3 = solution.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
    print(answer3)
