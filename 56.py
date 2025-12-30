from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merges all overlapping intervals.

        Args:
            intervals: A list of intervals where intervals[i] = [start, end].

        Returns:
            A list of merged non-overlapping intervals.
        """
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If merged is empty or no overlap with the last interval
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Overlap exists, merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged