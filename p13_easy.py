# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = ["I", "V", "X", "L", "C", "D", "M"]
        roman_val = [1, 5, 10, 50, 100, 500, 1000]
        sum_val = 0
        for x in range(len(s)):
            p = roman_num.index(s[x])
            if x != 0 and p != 0:
                if roman_num.index(s[x]) > roman_num.index(s[x-1]):
                    p2 = roman_num.index(s[x-1])
                    sum_val += roman_val[p] - (roman_val[p2] * 2)
                    continue
            sum_val += roman_val[p]

        return sum_val


if __name__ == "__main__":
    solution = Solution()
    answer = solution.romanToInt("LVIII")
    print(answer)
