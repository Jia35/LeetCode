# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    solution = Solution()
    answer = solution.isPalindrome(121)
    print(answer)
