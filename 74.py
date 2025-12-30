def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """Searches for a target value in an m x n matrix using binary search.

    The matrix is treated as a flattened 1D array to achieve logarithmic 
    time complexity, taking advantage of the row-wise and column-wise 
    sorting properties.

    Args:
        matrix: A 2D list of integers where each row is sorted and 
            the first element of a row is greater than the last of the previous.
        target: The integer value to search for.

    Returns:
        True if the target is found in the matrix, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Define the boundaries for binary search on a virtual 1D array
    low = 0
    high = (rows * cols) - 1

    while low <= high:
        mid = (low + high) // 2
        # Map 1D index back to 2D coordinates
        mid_val = matrix[mid // cols][mid % cols]

        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False