"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None
        
        nodes = {}       # map the node's value and the node's instance
        q = [node]       # for the BFS
        visited = set([node.val])
        
        while len(q) > 0:       # while we still have nodes to process
            
            currentToCopy = q.pop(0)            
            if currentToCopy.val not in nodes:        # create node's instance if it doesn't exist
                nodes[currentToCopy.val] = Node(currentToCopy.val)
            current = nodes[currentToCopy.val]        # get node's instance
        
            for neighbor in currentToCopy.neighbors:     # traverse through the current node's neighbors
                if neighbor.val not in nodes:            # create node's instance if it doesn't exist
                    nodes[neighbor.val] = Node(neighbor.val)
                current.neighbors.append(nodes[neighbor.val])    # append the neighbor to the current node
                if neighbor.val not in visited:
                    q.append(neighbor)           # append to queue only if it hasn't been visited
                visited.add(neighbor.val)        # add to visited nodes
                
        return nodes[node.val]     # return the given input node's new instance
        