# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #using bsf method and Big o(n)
         #check if the tree is not empty:if empty you return none
        # assign the  traverse to root
        #create three empty lists: level:for value in each level , next_level : save values for next level, reults: save the final values.
        #while the root exist you loop thru and add the nodes of each level to level
        #you add the subtree of each level to the next_level
        #you add the values the values in the level and divide it by the length
        #assign the traverse to the next_level
        #after that assign both level and next_level to empty list
        
        if not root:return None
        
        traverse = [root]
        level = []
        next_level = []
        results = []
        
        while traverse:
            for node in traverse:
                level.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            results.append(sum(level)/len(level))
            traverse = next_level
            next_level = []
            level = []
        return results
        