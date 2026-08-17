class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        curr_min = float('inf')
        for price in prices:
            if price < curr_min:
                curr_min = price
            else:
                best = max(best, price - curr_min)
        return best
