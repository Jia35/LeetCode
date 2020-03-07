# 27. Remove Element
# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    input1 = [3,2,2,3]
    answer1 = solution.removeElement(input1, 3)
    print(answer1)
    print(input1)

    input2 = [0,1,2,2,3,0,4,2]
    answer2 = solution.removeElement(input2, 2)
    print(answer2)
    print(input2)
