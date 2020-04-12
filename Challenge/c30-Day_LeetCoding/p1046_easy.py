# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/


from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stone1 = max(stones)
            stones.remove(stone1)
            stone2 = max(stones)
            stones.remove(stone2)
            
            diff_weight = abs(stone1 - stone2)
            if diff_weight > 0:
                stones.append(diff_weight)
        return stones[0] if len(stones) > 0 else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.lastStoneWeight([2,7,4,1,8,1]))
