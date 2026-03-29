# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        inorder_l = inorder[:root_index]
        inorder_r = inorder[root_index + 1 :]

        preorder_l = preorder[1: 1 + root_index]
        preorder_r = preorder[1 + root_index:]

        root.left = self.buildTree(preorder_l, inorder_l)
        root.right = self.buildTree(preorder_r, inorder_r)

        return root

