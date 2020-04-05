# 67. Add Binary
# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)
        return str(bin(num_a + num_b))[2:]


if __name__ == "__main__":
    solution = Solution()
    answer1 = solution.addBinary('11', '1')
    print(answer1)
    
    answer2 = solution.addBinary('1010', '1011')
    print(answer2)
