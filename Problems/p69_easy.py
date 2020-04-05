# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


if __name__ == "__main__":
    solution = Solution()
    answer1 = solution.mySqrt(4)
    print(answer1)
    
    answer2 = solution.mySqrt(8)
    print(answer2)
