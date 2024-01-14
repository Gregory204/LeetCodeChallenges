# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        mp = 0
        l = 0
        r = 1
        while r < len(prices):
            cur_pos = prices[r] - prices[l]
            if prices[l] < prices[r]:
                r += 1
            else:  # r > l
                l = r
                r += 1
            mp = max(cur_pos, mp)
        return mp

# 1 - 7 | 5 - 1
price = [1,2,4]
print(Solution().maxProfit(price))
# Output: 5
