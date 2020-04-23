# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 參考答案
        sums_so_far = defaultdict(int)
        our_sum = 0
        num_subarrays = 0
        for v in nums:
            our_sum += v
            if our_sum == k:
                num_subarrays += 1
            if (our_sum - k) in sums_so_far:
                num_subarrays += sums_so_far[our_sum - k]
            sums_so_far[our_sum] += 1
        return num_subarrays


if __name__ == "__main__":
    solution = Solution()
    answer = solution.subarraySum([9,2,1,3], 6)
    print(answer)
