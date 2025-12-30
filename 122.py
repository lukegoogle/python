from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculates max profit with an unlimited number of transactions.

        Args:
            prices: A list of integers representing stock prices per day.

        Returns:
            The total maximum profit accumulated from all upward trends.
        """
        max_total_profit = 0
        
        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                max_total_profit += prices[i] - prices[i - 1]
                
        return max_total_profit