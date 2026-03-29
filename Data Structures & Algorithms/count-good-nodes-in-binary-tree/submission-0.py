# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_so_far = -100
        count = 0
        def dfs(root, max_so_far):
            if not root:
                return 0
            
            count = 1 if root.val >= max_so_far else 0
            max_so_far = max(root.val, max_so_far)

            count += dfs(root.left, max_so_far)
            count += dfs(root.right, max_so_far)

            return count

        return dfs(root, max_so_far)