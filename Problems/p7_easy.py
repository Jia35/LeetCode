# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(abs(x))[::-1])
        if x < 0:
            y *= -1
        if (y > (2 ** 31 - 1)) or (y < -(2 ** 31)):
            return 0
        return y


if __name__ == "__main__":
    solution = Solution()
    answer = solution.reverse(123)
    print(answer)
