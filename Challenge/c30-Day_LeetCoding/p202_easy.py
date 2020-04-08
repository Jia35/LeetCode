# 202. Happy Number
# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        _temp_list = []
        while n != 1:
            n = sum([int(s) ** 2 for s in str(n)])
            if n in _temp_list:
                return False
            _temp_list.append(n)
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))
