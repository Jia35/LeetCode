# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)


if __name__ == "__main__":
    solution = Solution()
    answer1 = solution.strStr('hello', 'll')
    print(answer1)
    
    answer2 = solution.strStr('aaaaa', 'bba')
    print(answer2)
