def setZeroes(matrix: list[list[int]]) -> None:
    """Modifies the matrix in-place to set rows and columns to zero.

    If an element is 0, its entire row and column are set to 0. This 
    implementation uses the first row and first column as markers to 
    achieve O(1) auxiliary space complexity.

    Args:
        matrix: A 2D list of integers to be modified.

    Returns:
        None. The matrix is modified in-place.
    """
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False

    # Check if first row has any zeros
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break

    # Check if first column has any zeros
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break

    # Use first row and column as markers for the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out cells based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Finally, handle the first row and first column markers
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0