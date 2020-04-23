# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 參考答案
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i

        # result = list(bin(m)[2:])
        # for num in range(m, n+1):
        #     _num = bin(num)[2:]
        #     num = _num[(len(_num) - len(result)):]
        #     for i in range(len(num)):
        #         if (result[i] != '0') and (num[i] != '0'):
        #             result[i] = '1'
        #         else:
        #             result[i] = '0'
            
        #     if '1' not in result:
        #         return 0
        # return int(''.join(result), 2)

        # result = m
        # for num in range(m, n+1):
        #     result &= num
        # return result


if __name__ == "__main__":
    solution = Solution()
    # 600000000, 2147483645
    # answer = solution.rangeBitwiseAnd(0, 2147483647)
    answer = solution.rangeBitwiseAnd(5, 7)
    print(answer)
