# Leftmost Column with at Least a One
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/
from typing import List


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self):
        self.matrix = [
            [0,0,0,0,1,1],
            [0,0,0,1,1,1],
            [0,0,0,0,1,1],
            [0,0,0,0,0,0],
            [0,0,0,1,1,1],
            [0,0,0,1,1,1]
        ]
    
    def get(self, x: int, y: int) -> int:
       return self.matrix[x][y]
   
    def dimensions(self) -> List:
       return [6,6]

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # def find_letf_one(binaryMatrix, row):
        #     n, m = binaryMatrix.dimensions()
        #     start = 0
        #     end = m
        #     while start != end:
        #         mid = int((start + end) / 2)
        #         if binaryMatrix.get(row, mid) == 1:
        #             if mid == 0:
        #                 return mid
        #             if binaryMatrix.get(row, mid-1) == 0:
        #                 return mid
        #             else:
        #                 end = mid
        #         else:
        #             start = mid+1
        #     return -1

        # n, m = binaryMatrix.dimensions()
        # letf_one_num = -1
        # for row in range(n):
        #     letf_one = find_letf_one(binaryMatrix, row)
        #     if letf_one != -1:
        #         if (letf_one < letf_one_num) or (letf_one_num == -1):
        #             letf_one_num = letf_one
        # return letf_one_num

        # =============================
        n, m = binaryMatrix.dimensions()
        letf_one_num = m
        for row in range(n):
            while binaryMatrix.get(row, letf_one_num-1) == 1:
                letf_one_num -= 1
                if letf_one_num == 0:
                    return 0
        
        if letf_one_num == m:
            return -1
        return letf_one_num



if __name__ == "__main__":
    solution = Solution()
    binaryMatrix = BinaryMatrix()
    answer = solution.leftMostColumnWithOne(binaryMatrix)
    print(answer)
