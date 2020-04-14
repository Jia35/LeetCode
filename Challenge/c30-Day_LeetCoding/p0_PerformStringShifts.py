# Perform String Shifts
# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
# direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for _shift in shift:
            if _shift[0] == 0:
                move -= _shift[1]
            else:
                move += _shift[1]

        _move = abs(move) % len(s)
        if move > 0:
            _move = len(s) - _move
        
        return (s[_move:] + s[:_move])

        # move = 0
        # for _shift in shift:
        #     if _shift[0] == 0:
        #         move += _shift[1]
        #     else:
        #         move -= _shift[1]

        # move %= len(s)
        # return (s[move:] + s[:move])


if __name__ == "__main__":
    solution = Solution()
    answer = solution.stringShift("abc", [[0,1],[1,2]])
    print(answer)
