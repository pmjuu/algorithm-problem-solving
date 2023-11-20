"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_map = {}
        queue = [node]
        
        cloned_node = Node(node.val)
        node_map[node] = cloned_node
        
        while queue:
            current_node = queue.pop()
            
            for neighbor in current_node.neighbors:
                if neighbor not in node_map:
                    neighbor_clone = Node(neighbor.val)
                    node_map[neighbor] = neighbor_clone
                    queue.append(neighbor)

                node_map[current_node].neighbors.append(node_map[neighbor])
    
        return cloned_node