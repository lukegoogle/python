from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculates max profit with a limit of at most two transactions.

        This approach uses a state-machine DP to track the maximum balance
        after each of the four possible actions (buy1, sell1, buy2, sell2).

        Args:
            prices: A list of integers representing stock prices per day.

        Returns:
            The maximum total profit.
        """
        if not prices:
            return 0

        # We represent 'buy' as negative balance (money spent) 
        # and 'sell' as positive balance (profit made).
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # 1. Best balance after buying the first stock
            buy1 = max(buy1, -price)
            
            # 2. Best profit after selling the first stock
            sell1 = max(sell1, buy1 + price)
            
            # 3. Best balance after buying the second stock (using profit from sell1)
            buy2 = max(buy2, sell1 - price)
            
            # 4. Best final profit after selling the second stock
            sell2 = max(sell2, buy2 + price)

        return sell2