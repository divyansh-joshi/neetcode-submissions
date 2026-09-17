class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        sell = prices[1]
        answer = max(sell - buy, 0)
        for i in range(1, len(prices)):
            curr = prices[i]
            if buy > curr:
                buy = curr
                sell = curr
            if sell < curr:
                sell = curr

            answer = max(answer, sell-buy)
        return answer