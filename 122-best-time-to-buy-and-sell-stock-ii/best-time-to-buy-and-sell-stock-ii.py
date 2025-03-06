class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy_day, selling_day = 0, 0, 1

        while selling_day < len(prices):
            if prices[selling_day] >= prices[buy_day]:
                profit += prices[selling_day] - prices[buy_day]

            buy_day = selling_day
            selling_day += 1

        return profit