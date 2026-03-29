# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minNode(root: Optional[TreeNode]):
    curr = root
    while curr and curr.left:
        curr = curr.left

    return curr
    
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                mini = minNode(root.right)
                root.val = mini.val
                root.right = self.deleteNode(root.right,mini.val)

        return root
        