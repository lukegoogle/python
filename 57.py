from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Inserts a new interval into a sorted list and merges overlaps.

        Args:
            intervals: A list of non-overlapping intervals sorted by start time.
            newInterval: The interval [start, end] to be inserted.

        Returns:
            A new list of non-overlapping intervals in sorted order.
        """
        res = []
        i = 0
        n = len(intervals)
        
        # 1. Add all intervals that come before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 2. Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # 3. Add all remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res