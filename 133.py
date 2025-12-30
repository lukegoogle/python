from typing import Optional

class Node:
    """Definition for a Node."""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Creates a deep copy of a connected undirected graph.

        Args:
            node: The starting node of the graph to clone.

        Returns:
            The starting node of the cloned graph.
        """
        if not node:
            return None

        # Maps original node to its corresponding cloned node
        old_to_new = {}

        def dfs(curr_node: 'Node') -> 'Node':
            """Recursively clones nodes and their neighbors.

            Args:
                curr_node: The node in the original graph currently being cloned.

            Returns:
                The cloned version of the curr_node.
            """
            # If we already cloned this node, return the existing clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]

            # Create the clone (copy the value, but neighbors start empty)
            clone = Node(curr_node.val)
            old_to_new[curr_node] = clone

            # Iterate through the original neighbors and clone them
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)