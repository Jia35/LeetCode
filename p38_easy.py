# 38. Count and Say
# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:

        now_num = '1'
        for _ in range(n-1):
            n_list = now_num
            out_str = ''
            tmp_count = 0
            tmp = n_list[0]
            for unit in n_list:
                if unit == tmp:
                    tmp_count += 1
                else:
                    out_str += f'{tmp_count}{tmp}'
                    tmp = unit
                    tmp_count = 1
            out_str += f'{tmp_count}{tmp}'
            now_num = out_str
        return now_num



if __name__ == "__main__":
    solution = Solution()
    answer1 = solution.countAndSay(3)
    print(answer1)
    
    answer2 = solution.countAndSay(5)
    print(answer2)

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
