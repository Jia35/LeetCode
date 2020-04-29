# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/


class Solution(object):
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        c = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:
                    c[i+1][j+1] = c[i][j] + 1
                else:
                    c[i+1][j+1] = max(c[i][j+1], c[i+1][j])
        return c[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    text1 = "abcde"
    text2 = "ace"
    answer = solution.longestCommonSubsequence(text1, text2)
    print(answer)
