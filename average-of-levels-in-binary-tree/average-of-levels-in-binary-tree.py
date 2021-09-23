# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #use breath search first: we search by level traversal.
        
        if not root: return None
        level = []
        next_level = []
        result = []
        
        traverse = [root]
        
        while traverse:
            for node in traverse:
                level.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(sum(level)/len(level))
            traverse = next_level
            next_level = []
            level = []
        return result
            
        
        
        