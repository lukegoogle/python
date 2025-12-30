from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Determines the starting gas station index to complete a circular route.

        Args:
            gas: A list of integers representing gas available at each station.
            cost: A list of integers representing the cost to reach the next station.

        Returns:
            The starting gas station's index if the circuit can be completed, 
            otherwise -1.
        """
        # If total gas is less than total cost, a solution is impossible
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # If we run out of gas at this station
            if total_tank < 0:
                # We cannot start at any station from 'start_index' to 'i'
                # So we try starting at the next station
                start_index = i + 1
                total_tank = 0
                
        return start_index