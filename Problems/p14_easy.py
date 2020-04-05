# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        str_same = min(strs, key=len)
        for str_ in strs:
            str_tmp = ''
            for i, c in enumerate(str_same):
                if c == str_[i]:
                    str_tmp += c
                else:
                    break
            if str_tmp:
                str_same = str_tmp
            else:
                str_same = ''
        
        return str_same


if __name__ == "__main__":
    solution = Solution()
    input1 = ["flower", "flow", "flight"]
    answer1 = solution.longestCommonPrefix(input1)
    print(answer1)

    input2 = ["dog", "racecar", "car"]
    answer2 = solution.longestCommonPrefix(input2)
    print(answer2)
    