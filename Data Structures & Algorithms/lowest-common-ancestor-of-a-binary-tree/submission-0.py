# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        res = []
        
        def dfs(node):
            if node is None:
                return False

            left_has_target = dfs(node.left)
            right_has_target = dfs(node.right)
            current_is_target = node is p or node is q

            if left_has_target and right_has_target:
                res.append(node)
            elif current_is_target and (left_has_target or right_has_target):
                res.append(node)

            return current_is_target or left_has_target or right_has_target

        dfs(root)
        return res[0]