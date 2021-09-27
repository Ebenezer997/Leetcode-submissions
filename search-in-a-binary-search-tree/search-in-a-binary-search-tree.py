# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root: return None
        cur_node = root
        
        while cur_node:
            if val == cur_node.val:
                return cur_node
            
            elif val > cur_node.val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        return None
        
        