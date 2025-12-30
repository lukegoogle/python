def subsets(nums: list[int]) -> list[list[int]]:
    """Generates the power set of a list of unique integers.

    This function uses a backtracking approach to explore all possible 
    combinations of the input elements.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of lists containing all possible subsets.
    """
    results = []
    
    def backtrack(start: int, current_path: list[int]):
        # In the subsets problem, every path generated is a valid subset
        results.append(list(current_path))
        
        for i in range(start, len(nums)):
            # Include the number
            current_path.append(nums[i])
            # Move to the next index
            backtrack(i + 1, current_path)
            # Backtrack (remove the number)
            current_path.pop()

    backtrack(0, [])
    return results