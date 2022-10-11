"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraphNode(self, node: "Node", cloned_nodes={}):
        if node.val not in cloned_nodes: # not yet cloned
            cloned_nodes[node.val] = Node(node.val) # update dict
            for n in node.neighbors: # clone neighbors
                self.cloneGraphNode(n, cloned_nodes)
            cloned_nodes[node.val].neighbors = [cloned_nodes[n.val] for n in node.neighbors] # update neighbors with new refs
        return cloned_nodes[node.val]
        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        cloned_nodes = dict()
        self.cloneGraphNode(node, cloned_nodes)
        return cloned_nodes[node.val]