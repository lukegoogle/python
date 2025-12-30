class Solution:
    def numTrees(self, n: int) -> int:
        """Calculates the number of structurally unique BSTs with n nodes.

        Uses dynamic programming to solve the problem in O(n^2) time.

        Args:
            n: The number of nodes.

        Returns:
            The total number of unique BSTs.
        """
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        
        # Base cases: 
        # An empty tree (0 nodes) is one unique structure.
        # A tree with 1 node is one unique structure.
        dp[0] = 1
        dp[1] = 1
        
        # Fill the dp table for each number of nodes from 2 up to n
        for nodes in range(2, n + 1):
            for root_pos in range(1, nodes + 1):
                # left_nodes + right_nodes = nodes - 1
                left = root_pos - 1
                right = nodes - root_pos
                dp[nodes] += dp[left] * dp[right]
                
        return dp[n]