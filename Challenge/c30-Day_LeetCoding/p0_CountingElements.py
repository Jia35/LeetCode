# Counting Elements
# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for num in arr:
            if (num + 1) in arr:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    input_list = [1,1,2]
    print(solution.countElements(input_list))

    # [1,1,3,3,5,5,7,7]
    # [1,3,2,3,5,0]
    # [1,1,2,2]
