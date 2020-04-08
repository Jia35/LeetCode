# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = 0
        while n < len(prices)-1:
            if prices[n+1] < prices[n]:
                n += 1
                continue

            if (n+1) == len(prices):
                profit += (prices[n+1] - prices[n])
                break
            else:
                is_end = True
                for j in range(n+1, len(prices)-1):
                    # print(f'j: {j}')
                    if prices[j] > prices[j+1]:
                        profit += (prices[j] - prices[n])
                        is_end = False
                        n = j + 1
                        break
                
                if is_end:
                    profit += (prices[len(prices)-1] - prices[n])
                    break
        
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        max_list = []
        min_list = []
        profit = 0
        if len(prices) <= 1:
            return 0
        for i in range(len(prices)):
            if i == 0:
                if prices[i] >= prices[i+1]:
                    max_list.append(i)
                elif prices[i] <= prices[i+1]:
                    min_list.append(i)
            elif i == (len(prices)-1):
                if prices[i-1] <= prices[i]:
                    max_list.append(i)
                elif prices[i-1] >= prices[i]:
                    min_list.append(i)
            else:
                if (prices[i-1] <= prices[i]) and (prices[i] >= prices[i+1]):
                    max_list.append(i)
                elif (prices[i-1] >= prices[i]) and (prices[i] <= prices[i+1]):
                    min_list.append(i)

        # print(f'max_list: {max_list}')
        # print(f'min_list: {min_list}')

        for i in min_list:
            for j in range(i+1, max_list[-1]+1):
                if j in min_list:
                    break
                elif j in max_list:
                    profit += (prices[j] - prices[i])
                    break
        return profit

    def maxProfit3(self, prices: List[int]) -> int:
        # 參考別人
        max_profit = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


if __name__ == "__main__":
    solution = Solution()
    input_list = [1,3,8,7]
    print(solution.maxProfit(input_list))
    print(solution.maxProfit2(input_list))
    print(solution.maxProfit3(input_list))
