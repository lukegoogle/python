def minDistance(word1: str, word2: str) -> int:
    """Calculates the minimum edit distance between two strings.

    Uses a 2D dynamic programming table to find the minimum number of 
    insertions, deletions, or substitutions required to transform word1 
    into word2.

    Args:
        word1: The source string.
        word2: The target string.

    Returns:
        The integer representing the minimum number of operations.
    """
    m, n = len(word1), len(word2)
    
    # Create a DP table with (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: transforming a string to an empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],  # Replace
                    dp[i][j-1],    # Insert
                    dp[i-1][j]     # Delete
                )

    return dp[m][n]