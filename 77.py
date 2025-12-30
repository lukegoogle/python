def combine(n: int, k: int) -> list[list[int]]:
    """Generates all possible combinations of k numbers chosen from [1, n].

    Uses a backtracking algorithm to explore potential combinations,
    incorporating a pruning optimization to skip branches that cannot 
    yield a full combination of length k.

    Args:
        n: The upper bound of the range of numbers to choose from.
        k: The number of elements required in each combination.

    Returns:
        A list of lists, where each inner list is a valid combination.
    """
    result = []

    def backtrack(start: int, current_path: list[int]):
        # Base case: if the combination is the required length
        if len(current_path) == k:
            result.append(list(current_path))
            return

        # Optimization (Pruning):
        # We need (k - len(current_path)) more numbers.
        # If the remaining numbers in the range [start, n] are fewer 
        # than what we need, there's no point in continuing.
        need = k - len(current_path)
        remain = n - start + 1
        
        for i in range(start, n + 1):
            # Pruning check: if numbers left < numbers needed, break
            if n - i + 1 < need:
                break
                
            current_path.append(i)
            # Move to i + 1 to ensure we only pick numbers to the right (no duplicates)
            backtrack(i + 1, current_path)
            # Backtrack
            current_path.pop()

    backtrack(1, [])
    return result