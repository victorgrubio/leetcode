from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit :int = 0
        buy_price :int = prices[0]
        sell_price :int = 0
        for price in prices:
            if price < buy_price:
                if buy_price <= sell_price:
                    total_profit += (sell_price - buy_price)
                buy_price = price
                sell_price = price
            elif price > sell_price:
                sell_price = price
            elif price < sell_price:
                total_profit += (sell_price - buy_price)
                buy_price = price
                sell_price = 0
        if sell_price - buy_price > 0:
            total_profit += (sell_price - buy_price)
        return total_profit