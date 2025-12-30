from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculates the maximum profit possible from a single stock trade.

        Args:
            prices: A list of integers representing stock prices per day.

        Returns:
            The maximum profit possible. Returns 0 if no profit can be made.
        """
        # Initialize min_price to infinity and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price
            # Calculate profit if we sold at the current price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit