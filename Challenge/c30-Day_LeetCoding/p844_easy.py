# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def handle_str(input_str: str):
            _temp = []
            for c in input_str:
                if c == '#':
                    if _temp:
                        _temp.pop()
                else:
                    _temp.append(c)
            return ''.join(_temp)
        
        return (handle_str(S) == handle_str(T))

        # is_equal = True
        # n = len(S) - 1
        # m = len(T) - 1
        # while (n >= 0) or (m >= 0):
        #     i = 0
        #     while S[n] == '#':
        #         i += 1
        #         n -= 1
        #     n -= i

        #     i = 0
        #     while T[m] == '#':
        #         i += 1
        #         m -= 1
        #     m -= i

        #     if n < 0:
        #         _s = ''
        #     else:
        #         _s = S[n]
            
        #     if m < 0:
        #         _t = ''
        #     else:
        #         _t = T[m]

        #     if _s != _t:
        #         is_equal = False
        #         break

        #     if n >= 0:
        #         n -= 1
        #     if m >= 0:
        #         m -= 1
        
        # return is_equal


if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare(S="ab#c", T="ad#c"))
    # print(solution.backspaceCompare(S="y#fo##f", T="y#f#o##f"))
