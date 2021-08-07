# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        #check if the tree is not empty
        #you submit the values of the tree from the target sum at it traverses
        #if the root reach the leef node and target sume is zero
        # we does recursion for it to go again
        
        if not root: return False
        targetSum -= root.val
        
        if not root.left and not root.right and targetSum == 0:
            return True
        
        return (self.hasPathSum(root.left,targetSum)) or (self.hasPathSum(root.right,targetSum))