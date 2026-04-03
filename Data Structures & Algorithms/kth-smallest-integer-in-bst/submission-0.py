# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        listOut = []
        count
        def inOrder(root, listOut):
            if not root:
                return
            if len(listOut) == k:
                return
            inOrder(root.left, listOut)
            listOut.append(root.val)
            inOrder(root.right, listOut)
        
        listOut = []
        inOrder(root, listOut)
        return listOut[k - 1]


        